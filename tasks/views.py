from django.shortcuts import render
from django.utils import timezone
from .models import Task 
# Create your views here.

def task_list(request):
    tasks = Task.objects.filter(done_date__isnull=True).order_by('created_date')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})