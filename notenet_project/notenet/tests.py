from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
from .models import UserProfile, Material

class NoteNetTestCase(TestCase):
    def setUp(self):
        # Create user
        self.user = User.objects.create_user(username='alex', password='password123')
        self.profile, _ = UserProfile.objects.get_or_create(user=self.user)
        
    def test_profile_grade_display(self):
        self.profile.grade_number = 9
        self.profile.grade_letter = 'a'
        self.profile.save()
        self.assertEqual(self.profile.get_grade_display(), '9a')

    def test_grade_auto_advancement(self):
        # Set grade number and last updated to 365 days ago
        self.profile.grade_number = 9
        self.profile.grade_letter = 'a'
        self.profile.grade_updated_at = timezone.now() - datetime.timedelta(days=365)
        self.profile.save()
        
        # Check automatic increment
        advanced = self.profile.check_and_update_grade()
        self.assertTrue(advanced)
        self.assertEqual(self.profile.grade_number, 10)
        self.assertEqual(self.profile.grade_letter, 'a')
        
    def test_grade_access_restriction(self):
        # Set complete profile
        self.profile.full_name = 'Alex Georgiev'
        self.profile.grade_number = 9
        self.profile.grade_letter = 'a'
        self.profile.save()
        
        # Log in client
        client = Client()
        client.login(username='alex', password='password123')
        
        # Accessing Grade 9 should be OK
        response = client.get('/class/9/')
        self.assertEqual(response.status_code, 200)
        
        # Accessing Grade 8 should redirect to Grade 9!
        response = client.get('/class/8/')
        self.assertEqual(response.status_code, 302)
        self.assertTrue('/class/9/' in response.url)

