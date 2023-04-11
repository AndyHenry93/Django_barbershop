from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

# Test models.py
class ProfileModelTestcase(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User(first_name='Andy', last_name='Henry', email='andy.henry@gmail.com', username='Andy.henry')
        user.save()
        Profile.objects.create(user=user)

    def test_string_method(self):
        user_profile = Profile.objects.get()
        expected_string = user_profile.username
        self.assertEqual(str(user_profile),expected_string)
