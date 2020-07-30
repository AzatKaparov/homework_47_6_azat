from django.contrib import admin
from django.urls import path
from webapp.views import index_view, task_add_view, task_view, task_update_view, delete_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('tasks/add/', task_add_view, name='task_add'),
    path('task/<int:pk>/', task_view, name='task_view'),
    path('task/<int:pk>/update', task_update_view, name='task_update'),
    path('task/<int:pk>/delete', delete_view, name='task_delete')
]
