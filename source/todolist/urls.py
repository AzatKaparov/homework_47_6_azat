from django.contrib import admin
from django.urls import path
from webapp.views import index_view, task_add_view, delete, task_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('tasks/add/', task_add_view, name='task_add'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('task/<int:pk>/', task_view, name='task_view'),
]
