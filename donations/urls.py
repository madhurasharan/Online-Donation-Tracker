from django.urls import path
from . import views

urlpatterns = [
    path('checkout/<int:campaign_id>/', views.create_checkout_session, name='create_checkout_session'),
    path('stripe/webhook/', views.stripe_webhook, name='stripe_webhook'),
]
