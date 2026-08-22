from django.shortcuts import render
from .models import Profile, Skill, Education
from portfolio.models import Project, Certification, Experience, Testimonial

def home(request):
    try:
        profile = Profile.objects.first()
    except:
        profile = None
    
    featured_projects = Project.objects.filter(featured=True)[:6]
    certifications = Certification.objects.all()[:6]
    skills = Skill.objects.all()
    testimonials = Testimonial.objects.filter(featured=True)
    
    context = {
        'profile': profile,
        'projects': featured_projects,
        'certifications': certifications,
        'skills': skills,
        'testimonials': testimonials,
    }
    return render(request, 'core/home.html', context)

def about(request):
    try:
        profile = Profile.objects.first()
    except:
        profile = None
    
    education = Education.objects.all()
    experiences = Experience.objects.all()
    skills = Skill.objects.all()
    
    context = {
        'profile': profile,
        'education': education,
        'experiences': experiences,
        'skills': skills,
    }
    return render(request, 'core/about.html', context)

def contact(request):
    try:
        profile = Profile.objects.first()
    except:
        profile = None
    
    context = {
        'profile': profile,
    }
    return render(request, 'core/contact.html', context)