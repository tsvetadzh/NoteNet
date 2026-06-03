from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
import os

def material_file_upload_path(instance, filename):
    date_str = timezone.now().strftime('%Y-%m-%d')
    return f"materials/{date_str}_{filename}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=150, blank=True)
    grade_number = models.IntegerField(null=True, blank=True)  # 8, 9, 10, 11, 12
    grade_letter = models.CharField(max_length=10, blank=True)  # 'a', 'b', 'c', 'd', etc.
    grade_updated_at = models.DateTimeField(default=timezone.now)

    def get_grade_display(self):
        if self.grade_number and self.grade_letter:
            return f"{self.grade_number}{self.grade_letter}"
        return ""

    def check_and_update_grade(self):
        # Check if 365 days have passed since grade_updated_at
        now = timezone.now()
        delta = now - self.grade_updated_at
        if delta.days >= 365:
            # How many periods of 365 days have passed
            years_passed = delta.days // 365
            if years_passed > 0:
                if self.grade_number:
                    new_grade = self.grade_number + years_passed
                    if new_grade > 12:
                        new_grade = 12  # cap at 12
                    self.grade_number = new_grade
                    # Update grade_updated_at by adding the exact number of years
                    self.grade_updated_at = self.grade_updated_at + datetime.timedelta(days=365 * years_passed)
                    self.save()
                    return True
        return False

    def __str__(self):
        return f"{self.user.username}'s Profile ({self.get_grade_display() or 'No Grade'})"


class Material(models.Model):
    title = models.CharField(max_length=255, blank=True)
    grade = models.IntegerField()  # 8, 9, 10, 11, 12
    section = models.CharField(max_length=10)  # 'a', 'b', 'c', 'd', etc.
    subject = models.CharField(max_length=100)  # slug, e.g. 'biology'
    description = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='materials')

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return f"{self.subject} ({self.grade}{self.section}) - {self.description[:20]}"


class MaterialFile(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to=material_file_upload_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['uploaded_at']

    @property
    def filename(self):
        return os.path.basename(self.file.name)

    @property
    def display_name(self):
        basename = os.path.basename(self.file.name)
        # Check if it has a prefix like YYYY-MM-DD_ (11 characters)
        if len(basename) > 11 and basename[4] == '-' and basename[7] == '-' and basename[10] == '_':
            return basename[11:]
        return basename

    @property
    def is_image(self):
        ext = os.path.splitext(self.file.name)[1].lower()
        return ext in ['.png', '.jpg', '.jpeg', '.gif', '.webp']

    def __str__(self):
        return f"File for {self.material} - {self.display_name}"


