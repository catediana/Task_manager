from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, TaskForm, SubtaskForm, ProfileForm, CategoryForm, CommentForm
from .models import Task, Category, Subtask, UserProfile, Comment
from django.db.models import Q
from django.http import JsonResponse
from datetime import date, timedelta

# Create your views here.

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("task_list")  # Redirect to task list after registration
    else:
        form = RegisterForm()
    return render(request, "tasks/register.html", {"form": form})

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("task_list") # Redirect to task list after login
    else:
        form = AuthenticationForm()
    return render(request, "tasks/login.html", {"form": form})

def user_logout(request):
    logout(request)
    return redirect("user_login") # Redirect to login page after logout

@login_required
def task_list(request):
    show_archived = request.GET.get('show_archived', 'false').lower() == 'true'
    
    if show_archived:
        tasks = Task.objects.filter(user=request.user)
    else:
        tasks = Task.objects.filter(user=request.user, is_archived=False)

    # Reminder Logic
    today = date.today()
    three_days_from_now = today + timedelta(days=3)
    tomorrow = today + timedelta(days=1)

    # Overdue tasks (not complete and not archived)
    overdue_tasks = Task.objects.filter(
        user=request.user,
        due_date__lt=today,
        status__in=['pending', 'in_progress'],
        is_archived=False
    ).order_by('due_date')

    # Tasks due today (not complete and not archived)
    tasks_due_today = Task.objects.filter(
        user=request.user,
        due_date=today,
        status__in=['pending', 'in_progress'],
        is_archived=False
    ).order_by('priority')

    # Tasks due tomorrow (not complete and not archived)
    tasks_due_tomorrow = Task.objects.filter(
        user=request.user,
        due_date=tomorrow,
        status__in=['pending', 'in_progress'],
        is_archived=False
    ).order_by('priority')

    # Tasks due within the next 3 days (excluding today and tomorrow, not complete and not archived)
    tasks_due_soon = Task.objects.filter(
        user=request.user,
        due_date__gt=tomorrow,
        due_date__lte=three_days_from_now,
        status__in=['pending', 'in_progress'],
        is_archived=False
    ).order_by('due_date')

    # Search
    search_query = request.GET.get('search')
    if search_query:
        tasks = tasks.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))

    # Filter by Status
    status_filter = request.GET.get('status')
    if status_filter and status_filter != 'all':
        tasks = tasks.filter(status=status_filter)

    # Filter by Priority
    priority_filter = request.GET.get('priority')
    if priority_filter and priority_filter != 'all':
        tasks = tasks.filter(priority=priority_filter)

    # Filter by Category
    category_filter = request.GET.get('category')
    if category_filter and category_filter != 'all':
        tasks = tasks.filter(category__id=category_filter)

    # Filter by Due Date
    due_date_filter = request.GET.get('due_date_filter')
    if due_date_filter == 'overdue':
        tasks = tasks.filter(due_date__lt=today, status__in=['pending', 'in_progress'])
    elif due_date_filter == 'today':
        tasks = tasks.filter(due_date=today)
    elif due_date_filter == 'this_week':
        start_of_week = today - timedelta(days=today.weekday())
        end_of_week = start_of_week + timedelta(days=6)
        tasks = tasks.filter(due_date__range=[start_of_week, end_of_week])
    elif due_date_filter == 'next_week':
        start_of_next_week = today + timedelta(days=(7 - today.weekday()) % 7)
        end_of_next_week = start_of_next_week + timedelta(days=6)
        tasks = tasks.filter(due_date__range=[start_of_next_week, end_of_next_week])

    # Sorting (already handled by model Meta, but can be overridden by GET param)
    sort_by = request.GET.get('sort_by', 'position') # Default sort by position
    tasks = tasks.order_by(sort_by)

    categories = Category.objects.filter(user=request.user)

    context = {
        'tasks': tasks,
        'categories': categories,
        'search_query': search_query,
        'status_filter': status_filter,
        'priority_filter': priority_filter,
        'category_filter': category_filter,
        'due_date_filter': due_date_filter,
        'sort_by': sort_by,
        'task_status_choices': Task.STATUS_CHOICES,
        'task_priority_choices': Task.PRIORITY_CHOICES,
        'overdue_tasks': overdue_tasks,
        'tasks_due_today': tasks_due_today,
        'tasks_due_soon': tasks_due_soon,
        'tasks_due_tomorrow': tasks_due_tomorrow,
        'show_archived': show_archived,
    }
    return render(request, 'tasks/task_list.html', context)

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST, user=request.user)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm(user=request.user)
    return render(request, 'tasks/add_task.html', {'form': form})

@login_required
def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    comments = task.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.task = task
            comment.user = request.user
            comment.save()
            return redirect('task_detail', task_id=task.id)
    else:
        form = CommentForm()
    return render(request, 'tasks/task_detail.html', {'task': task, 'comments': comments, 'comment_form': form})

@login_required
def add_comment(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.task = task
            comment.user = request.user
            comment.save()
    return redirect('task_detail', task_id=task.id)

@login_required
def archive_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.is_archived = True
    task.save()
    return redirect('task_list')

@login_required
def unarchive_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.is_archived = False
    task.save()
    return redirect('task_list')

@login_required
def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    subtasks = task.subtasks.all()
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES, instance=task, user=request.user)
        subtask_forms = [SubtaskForm(request.POST, instance=s, prefix=f'subtask-{s.id}') for s in subtasks]
        if form.is_valid() and all(sf.is_valid() for sf in subtask_forms):
            form.save()
            for sf in subtask_forms:
                sf.save()
            # Handle new subtask if submitted
            new_subtask_title = request.POST.get('new_subtask_title')
            if new_subtask_title:
                Subtask.objects.create(task=task, title=new_subtask_title)
            return redirect('task_list')
    else:
        form = TaskForm(instance=task, user=request.user)
        subtask_forms = [SubtaskForm(instance=s, prefix=f'subtask-{s.id}') for s in subtasks]
    return render(request, 'tasks/update_task.html', {'form': form, 'task': task, 'subtasks': subtasks, 'subtask_forms': subtask_forms})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    return redirect('task_list')

@login_required
def category_list(request):
    categories = Category.objects.filter(user=request.user).order_by('name')
    return render(request, 'tasks/category_list.html', {'categories': categories})

@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'tasks/add_category.html', {'form': form})

@login_required
def category_update(request, category_id):
    category = get_object_or_404(Category, id=category_id, user=request.user)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'tasks/category_update.html', {'form': form, 'category': category})

@login_required
def category_delete(request, category_id):
    category = get_object_or_404(Category, id=category_id, user=request.user)
    category.delete()
    return redirect('category_list')

@login_required
def update_task_status_ajax(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        task_id = request.POST.get('task_id')
        new_status = request.POST.get('status')
        try:
            task = Task.objects.get(id=task_id, user=request.user)
            task.status = new_status
            task.save()
            return JsonResponse({'success': True})
        except Task.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Task not found'}, status=404)
    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)

@login_required
def add_subtask(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        form = SubtaskForm(request.POST)
        if form.is_valid():
            subtask = form.save(commit=False)
            subtask.task = task
            subtask.save()
            return redirect('update_task', task_id=task.id)
    return redirect('update_task', task_id=task.id) # Or render a specific add_subtask.html

@login_required
def toggle_subtask_complete(request, subtask_id):
    subtask = get_object_or_404(Subtask, id=subtask_id, task__user=request.user)
    subtask.complete = not subtask.complete
    subtask.save()
    return redirect('update_task', task_id=subtask.task.id)

@login_required
def delete_subtask(request, subtask_id):
    subtask = get_object_or_404(Subtask, id=subtask_id, task__user=request.user)
    task_id = subtask.task.id
    subtask.delete()
    return redirect('update_task', task_id=task_id)

@login_required
def reorder_tasks_ajax(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        task_ids = request.POST.getlist('task_ids[]')
        for index, task_id in enumerate(task_ids):
            try:
                task = Task.objects.get(id=task_id, user=request.user)
                task.position = index
                task.save()
            except Task.DoesNotExist:
                return JsonResponse({'success': False, 'error': f'Task with ID {task_id} not found.' }, status=404)
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)

@login_required
def profile_settings(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_settings')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'tasks/profile_settings.html', {'form': form, 'profile': profile})
