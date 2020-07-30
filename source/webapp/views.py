from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Task
from django.http import HttpResponseNotFound, HttpResponseNotAllowed
from .forms import TaskForm


def index_view(request):
    data = Task.objects.all()
    return render(request, 'index.html', context={
        'tasks': data
    })


def task_add_view(request, *args, **kwargs):
    if request.method == "GET":
        form = TaskForm()
        return render(request, 'task_add.html', context={
            'form': form
        })
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = Task.objects.create(
                description=form.cleaned_data['description'],
                more=form.cleaned_data['more'],
                date=form.cleaned_data['date'],
                status=form.cleaned_data['status']
            )
        else:
            return render(request, 'task_add.html', context={
                'form': form
            })

        return redirect('task_view', pk=task.pk)


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


def delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'task': task})
    elif request.method == 'POST':
        task.delete()
        return redirect('index')
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])


def task_update_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "GET":
        form = TaskForm(initial={
            'description': task.description,
            'more': task.more,
            'status': task.status,
            'date': task.date
        })
        return render(request, 'update.html', context={
            'form': form,
            'task': task
        })
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.description = form.cleaned_data['description']
            task.more = form.cleaned_data['more']
            task.status = form.cleaned_data['status']
            task.date = form.cleaned_data['date']
            task.save()
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'update.html', context={
                'task': task,
                'form': form,
                'errors': form.errors
            })
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])


# def task_update_view(request, pk):
#     task = get_object_or_404(Task, pk=pk)
#     if request.method =='GET':
#         return render(request, 'update.html', context={
#             'status_choices': STATUS_CHOICES,
#             'task': task,
#         })
#     elif request.method =='POST':
#         errors = {}
#         task.description = request.POST.get('description')
#         if not task.description:
#             errors['description'] = "Это поле обязательно!"
#         task.status = request.POST.get('status')
#         if not task.status:
#             errors['status'] = "Это поле обязательно!"
#         task.date = request.POST.get('date')
#         if not task.date:
#             errors['date'] = "Это поле обязательно!"
#         task.more = request.POST.get('more')
#
#         if errors:
#             return render(request, 'update.html', context={
#                 'status_choices': STATUS_CHOICES,
#                 'task': task,
#                 'errors': errors,
#             })
#         task.save()
#
#         return redirect('task_view', pk=task.pk)