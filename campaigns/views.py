from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Campaign
from .serializers import CampaignSerializer

class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer