from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth import get_user_model
from campaigns.models import Campaign
from .models import Donation
from django.utils import timezone
from datetime import timedelta

User = get_user_model()

class DonationModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='donor', password='pass')
        self.campaign = Campaign.objects.create(
            owner=self.user,
            title='Save Trees',
            description='Plant trees for the planet',
            target_amount=5000.00,
            deadline=timezone.now() + timedelta(days=30)
        )

    def test_donation_create(self):
        d = Donation.objects.create(
            campaign=self.campaign,
            donor=self.user,
            amount=100.00
        )
        self.assertEqual(d.amount, 100.00)
