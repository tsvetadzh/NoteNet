from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
from .models import UserProfile, Material, MaterialFile

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

    def test_material_upload_multiple_files(self):
        # Set complete profile
        self.profile.full_name = 'Alex Georgiev'
        self.profile.grade_number = 9
        self.profile.grade_letter = 'a'
        self.profile.save()

        # Log in client
        client = Client()
        client.login(username='alex', password='password123')

        # Create two simple mock files
        from django.core.files.uploadedfile import SimpleUploadedFile
        file1 = SimpleUploadedFile("notes1.txt", b"Notes content 1")
        file2 = SimpleUploadedFile("photo1.jpg", b"fake image bytes")

        # Post request to upload_material
        url = '/class/9/biology/upload/'
        response = client.post(url, {
            'description': 'Test material description',
            'section': 'a',
            'files': [file1, file2]
        }, HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['success'])

        # Verify Material and MaterialFiles created
        material = Material.objects.first()
        self.assertIsNotNone(material)
        self.assertEqual(material.description, 'Test material description')
        self.assertEqual(material.files.count(), 2)

        # Verify filename prepending with date
        files_list = list(material.files.all())
        date_str = timezone.now().strftime('%Y-%m-%d')
        
        self.assertEqual(files_list[0].display_name, 'notes1.txt')
        self.assertEqual(files_list[1].display_name, 'photo1.jpg')
        self.assertTrue(files_list[0].filename.startswith(date_str))
        self.assertTrue(files_list[1].filename.startswith(date_str))
        self.assertFalse(files_list[0].is_image)
        self.assertTrue(files_list[1].is_image)

    def test_materials_ordering_newest_first(self):
        # Create two materials at different times
        m1 = Material.objects.create(
            grade=9, section='a', subject='biology',
            description='First material', uploaded_by=self.user
        )
        # Manually alter uploaded_at for m1 to be in the past
        Material.objects.filter(id=m1.id).update(uploaded_at=timezone.now() - datetime.timedelta(hours=1))

        m2 = Material.objects.create(
            grade=9, section='a', subject='biology',
            description='Second material', uploaded_by=self.user
        )

        materials = list(Material.objects.filter(grade=9, subject='biology'))
        self.assertEqual(materials[0].description, 'Second material')
        self.assertEqual(materials[1].description, 'First material')


