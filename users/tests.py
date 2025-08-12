from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class UserModelTests(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(
            username='testuser',
            password='testpass',
            role='donor'
        )
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.role, 'donor')
