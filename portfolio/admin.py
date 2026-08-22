from django.contrib import admin
from .models import Project, Certification, Experience, Testimonial

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'featured', 'created_at']
    list_filter = ['status', 'featured']
    search_fields = ['title', 'description']

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ['name', 'organization', 'issue_date']
    search_fields = ['name', 'organization']

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['company', 'position', 'start_date', 'current']
    list_filter = ['current']

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'company', 'featured']
    list_filter = ['featured']