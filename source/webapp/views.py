from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Task, STATUS_CHOICES
from django.http import HttpResponseNotFound, HttpResponseRedirect, HttpResponseNotAllowed
from django.urls import reverse


def index_view(request):
    data = Task.objects.all()
    return render(request, 'index.html', context={
        'tasks': data
    })


def task_add_view(request, *args, **kwargs):
    if request.method == "GET":
        return render(request, 'task_add.html', context={
            'status_choices': STATUS_CHOICES
        })
    elif request.method == 'POST':
        description = request.POST.get('description')
        status = request.POST.get('status')
        date = request.POST.get('date')
        more = request.POST.get('more')
        task = Task.objects.create(description=description, status=status, date=date, more=more)
        url = reverse('task_view', kwargs={'pk': task.pk})
        return HttpResponseRedirect(url)


def delete(request, pk):
    try:
        task = Task.objects.get(pk=pk)
        task.delete()
        return redirect('index')
    except Task.DoesNotExist:
        return HttpResponseNotFound("<h2>Task not found</h2>")


def task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    context = {'task': task}
    return render(request, 'task_view.html', context)


def task_update_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method =='GET':
        return render(request, 'update.html', context={
            'status_choices': STATUS_CHOICES,
            'task': task,
        })
    elif request.method =='POST':
        errors = {}
        task.description = request.POST.get('description')
        if not task.description:
            errors['description'] = "Это поле обязательно!"
        task.status = request.POST.get('status')
        if not task.status:
            errors['status'] = "Это поле обязательно!"
        task.date = request.POST.get('date')
        if not task.date:
            errors['date'] = "Это поле обязательно!"
        task.more = request.POST.get('more')

        if errors:
            return render(request, 'update.html', context={
                'status_choices': STATUS_CHOICES,
                'task': task,
                'errors': errors,
            })
        task.save()

        return redirect('task_view', pk=task.pk)


def delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'task': task})
    elif request.method == 'POST':
        task.delete()
        return redirect('index')
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])
