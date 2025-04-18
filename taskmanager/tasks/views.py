from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Task, Category
from .forms import TaskForm, SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect


@login_required
def index(request):
    tasks = Task.objects.filter(user=request.user)
    status = request.GET.get('status')
    category = request.GET.get('category')
    search = request.GET.get('search')

    if status == 'completed':
        tasks = tasks.filter(completed=True)
    elif status == 'pending':
        tasks = tasks.filter(completed=False)

    if category:
        tasks = tasks.filter(category__name=category)

    if search:
        tasks = tasks.filter(title__icontains=search)

    categories = Category.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'categories': categories})


@login_required
def create_task(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        task = form.save(commit=False)
        task.user = request.user
        task.save()
        return redirect('index')
    return render(request, 'tasks/task_form.html', {'form': form})


@login_required
def update_task(request, pk):
    task = Task.objects.get(id=pk, user=request.user)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'tasks/task_form.html', {'form': form})


@login_required
def delete_task(request, pk):
    task = Task.objects.get(id=pk, user=request.user)
    task.delete()
    return redirect('index')


def signup_view(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('index')
    return render(request, 'tasks/signup.html', {'form': form})


def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'log_in.html', {'form': form})


def log_out(request):
    logout(request)
    return HttpResponseRedirect('/login/')


@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user)
    total_tasks = tasks.count()
    completed_tasks = tasks.filter(completed=True).count()
    pending_tasks = tasks.filter(completed=False).count()

    context = {
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks
    }
    return render(request, 'tasks/dashboard.html', context)


def view_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'tasks/view_tasks.html', {'task': task})
