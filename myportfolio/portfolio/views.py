from django.http import JsonResponse
from django.shortcuts import redirect, render
from .models import Project, Skill
from .forms import ContactForm
from .tasks import execute_calculator, long_running_task
from celery.result import AsyncResult

def home(request):
    """
    Home view that triggers the calculator task asynchronously.
    """
    task_result = execute_calculator.delay()
    context = {
        'task_id': task_result.id
    }
    return render(request, 'portfolio/home.html', context)

def get_task_status(request, task_id):
    """
    View to check the status of an asynchronous task.
    """
    # task = execute_calculator.AsyncResult(task_id)
    # if task.state == 'SUCCESS':
    #     output = task.get()
    #     return JsonResponse({'status': 'success', 'output': output})
    # elif task.state == 'FAILURE':
    #     return JsonResponse({'status': 'failure', 'message': 'Task failed to execute'})
    # else:
    #     return JsonResponse({'status': 'pending'})
    try: 
        task = Task.objects.get(id=task_id)
        status = task.status
        return JsonResponse({'status': status})
    except Task.DoesNotExist:
        return JsonResponse({'status': 'Task not found'}, status=404)

def start_task(request):
    task = long_running_task.delay('some_param')
    return JsonResponse({'task_id': task.id})

def get_task_status(request, task_id):
    result = AsyncResult(task_id)
    status = result.status
    result_data = result.result if result.ready() else None
    return JsonResponse({'status': status, 'result': result_data})

def projects(request):
    """
    View to display all projects.
    """
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'portfolio/projects.html', context)

def skills(request):
    """
    View to display all skills.
    """
    skills = Skill.objects.all()
    context = {
        'skills': skills
    }
    return render(request, 'portfolio/skills.html', context)

def contact(request):
    """
    View to handle contact form submissions.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('portfolio:skills')
    else:
        form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'portfolio/contact.html', context)
