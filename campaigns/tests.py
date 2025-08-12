from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Campaign
from django.utils import timezone
from datetime import timedelta

User = get_user_model()

class CampaignModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='u1', password='pass')

    def test_campaign_create(self):
        c = Campaign.objects.create(
            owner=self.user,
            title='Test',
            description='desc',
            target_amount=100.00,
            deadline=timezone.now() + timedelta(days=10)
        )
        self.assertEqual(str(c), 'Test')
