from django.shortcuts import render, get_object_or_404
from .models import Project, Certification

def project_list(request):
    """View to display all projects"""
    projects = Project.objects.all().order_by('-created_at')
    context = {
        'projects': projects,
    }
    return render(request, 'portfolio/project_list.html', context)

def project_detail(request, pk):
    """View to display a single project"""
    project = get_object_or_404(Project, pk=pk)
    context = {
        'project': project,
    }
    return render(request, 'portfolio/project_detail.html', context)

def certification_list(request):
    """View to display all certifications"""
    certifications = Certification.objects.all().order_by('-issue_date')
    context = {
        'certifications': certifications,
    }
    return render(request, 'portfolio/certification_list.html', context)