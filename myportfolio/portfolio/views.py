import subprocess
from django.shortcuts import HttpResponse, redirect, render
from .models import Project, Skill
from .forms import ContactForm

# Create your views here.

def home(request):
    try:
        result = subprocess.run(['c_programs/calculator.exe'], capture_output=True, text=True, timeout=10)  # Increase timeout as needed
    except subprocess.TimeoutExpired:
        return HttpResponse("Execution timed out. Please try again later.")
    except FileNotFoundError:
        return HttpResponse("Executable file not found.")
    except Exception as e:
        return HttpResponse(f"An error occurred: {e}")

    if result.returncode != 0:
        return HttpResponse(f"Execution failed with return code {result.returncode}")

    output = result.stdout

    context = {
        'output': output
    }
    return render(request, 'portfolio/home.html', context)


# def home(request): 
#     #Executing the c calculator program
#     result = subprocess.run(['c_programs/calculator.exe'], capture_output=True,text=True)
    
#     #Capturing the output from the c calculator program
#     output = result.stdout
    
#     context = {
#         'output': output
#     }
#     return render(request, 'portfolio/home.html', context)


# def home(request):
    
#     result = subprocess.run(['echo', '<h1>Hello, world!</h1>'], capture_output=True, text=True, timeout=5)    
       

#     output = result.stdout

#     context = {
#         'output': output
#     }
#     return render(request, 'portfolio/home.html', context)

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
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('portfolio/skills.html')
    else:
        form = ContactForm()
    
    context = {
        'form': form
    }
    return render(request, 'portfolio/contact.html', context)
    