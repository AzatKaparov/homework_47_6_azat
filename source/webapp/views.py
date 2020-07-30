from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Task, STATUS_CHOICES
from django.http import HttpResponseNotFound, HttpResponseRedirect
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