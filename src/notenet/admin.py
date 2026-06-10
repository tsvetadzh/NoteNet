from django.contrib import admin
from .models import UserProfile, Material, MaterialFile

class MaterialFileInline(admin.TabularInline):
    model = MaterialFile
    extra = 1

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'grade_number', 'grade_letter', 'grade_updated_at')
    search_fields = ('user__username', 'full_name', 'grade_letter')

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('subject', 'grade', 'section', 'uploaded_by', 'uploaded_at')
    list_filter = ('grade', 'section', 'subject')
    search_fields = ('description', 'subject', 'uploaded_by__username')
    inlines = [MaterialFileInline]


