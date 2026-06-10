import datetime

from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils import timezone

from notenet.models import UserProfile, Material, MaterialFile


class UserProfileTests(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username='alex', password='password123')
        self.profile, _ = UserProfile.objects.get_or_create(user=self.user)

    def test_grade_display(self) -> None:
        self.profile.grade_number = 9
        self.profile.grade_letter = 'a'
        self.profile.save()
        self.assertEqual(self.profile.get_grade_display(), '9a')

    def test_grade_display_empty_when_no_grade(self) -> None:
        self.assertEqual(self.profile.get_grade_display(), '')

    def test_grade_auto_advancement(self) -> None:
        self.profile.grade_number = 9
        self.profile.grade_letter = 'a'
        self.profile.grade_updated_at = timezone.now() - datetime.timedelta(days=365)
        self.profile.save()
        advanced = self.profile.check_and_update_grade()
        self.assertTrue(advanced)
        self.assertEqual(self.profile.grade_number, 10)

    def test_grade_does_not_advance_early(self) -> None:
        self.profile.grade_number = 9
        self.profile.grade_letter = 'a'
        self.profile.grade_updated_at = timezone.now() - datetime.timedelta(days=100)
        self.profile.save()
        advanced = self.profile.check_and_update_grade()
        self.assertFalse(advanced)
        self.assertEqual(self.profile.grade_number, 9)

    def test_grade_capped_at_12(self) -> None:
        self.profile.grade_number = 12
        self.profile.grade_letter = 'a'
        self.profile.grade_updated_at = timezone.now() - datetime.timedelta(days=365)
        self.profile.save()
        self.profile.check_and_update_grade()
        self.assertEqual(self.profile.grade_number, 12)


class AccessControlTests(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username='alex', password='password123')
        self.profile, _ = UserProfile.objects.get_or_create(user=self.user)
        self.profile.full_name = 'Alex Georgiev'
        self.profile.grade_number = 9
        self.profile.grade_letter = 'a'
        self.profile.save()
        self.client = Client()
        self.client.login(username='alex', password='password123')

    def test_can_access_own_grade(self) -> None:
        response = self.client.get('/class/9/')
        self.assertEqual(response.status_code, 200)

    def test_redirected_from_other_grade(self) -> None:
        response = self.client.get('/class/8/')
        self.assertEqual(response.status_code, 302)
        self.assertIn('/class/9/', response.url)


class MaterialTests(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username='alex', password='password123')
        self.profile, _ = UserProfile.objects.get_or_create(user=self.user)
        self.profile.full_name = 'Alex Georgiev'
        self.profile.grade_number = 9
        self.profile.grade_letter = 'a'
        self.profile.save()
        self.client = Client()
        self.client.login(username='alex', password='password123')

    def test_upload_creates_material(self) -> None:
        file1 = SimpleUploadedFile("notes.txt", b"some content")
        response = self.client.post('/class/9/biology/upload/', {
            'description': 'Biology notes',
            'section': 'a',
            'files': [file1],
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Material.objects.filter(description='Biology notes').exists())

    def test_upload_multiple_files(self) -> None:
        file1 = SimpleUploadedFile("notes.txt", b"content 1")
        file2 = SimpleUploadedFile("photo.jpg", b"content 2")
        self.client.post('/class/9/biology/upload/', {
            'description': 'Two files',
            'section': 'a',
            'files': [file1, file2],
        })
        material = Material.objects.get(description='Two files')
        self.assertEqual(material.files.count(), 2)

    def test_materials_ordered_newest_first(self) -> None:
        old = Material.objects.create(
            grade=9, section='a', subject='biology',
            description='Old material', uploaded_by=self.user
        )
        Material.objects.filter(id=old.id).update(
            uploaded_at=timezone.now() - datetime.timedelta(hours=1)
        )
        Material.objects.create(
            grade=9, section='a', subject='biology',
            description='New material', uploaded_by=self.user
        )
        materials = list(Material.objects.filter(grade=9, subject='biology'))
        self.assertEqual(materials[0].description, 'New material')
        self.assertEqual(materials[1].description, 'Old material')
