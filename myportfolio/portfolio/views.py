from django.shortcuts import render
from .models import Project, Skill

# Create your views here.
def home(request): 
    return render(request, 'portfolio/home.html')

def projects(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
        }
    return render(request, 'portfolio/projects.html', context)

def skills(request):
    skills = Skill.objects.all()
    context = {
        'skills': skills
        }
    return render(request, 'portfolio/skills.html', context)

def contact(request):
    return render(request, 'portfolio/contact.html')
    