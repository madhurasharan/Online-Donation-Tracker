import json
import stripe
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .models import Campaign, Donation
from payments.utils import create_stripe_checkout_session
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

stripe.api_key = settings.STRIPE_SECRET_KEY

@api_view(['POST'])
def create_checkout_session(request, campaign_id):
    try:
        campaign = Campaign.objects.get(id=campaign_id)
        amount = request.data.get('amount')
        
        session = create_stripe_checkout_session(
            campaign,
            float(amount),
            success_url=request.build_absolute_uri('/success'),
            cancel_url=request.build_absolute_uri('/cancel')
        )
        return JsonResponse({'id': session.id})
    except Campaign.DoesNotExist:
        return JsonResponse({'error': 'Campaign not found'}, status=404)

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    endpoint_secret = settings.STRIPE_WEBHOOK_SECRET

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
    except ValueError:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        campaign_id = session['metadata']['campaign_id']
        amount = session['amount_total'] / 100

        # Save donation
        campaign = Campaign.objects.get(id=campaign_id)
        Donation.objects.create(campaign=campaign, amount=amount)

        # Broadcast update via Channels
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f"campaign_{campaign_id}",
            {
                'type': 'donation_update',
                'message': f'New donation of ${amount} received!'
            }
        )

    return HttpResponse(status=200)
