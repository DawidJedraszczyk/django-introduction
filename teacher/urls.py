from django.urls import path
from . import views

urlpatterns = [
    path('', views.teacher_list, name='teacher_list'),
    path('new/', views.create_teacher, name='create_teacher'),
    path('delete/<int:teacher_id>/', views.delete_teacher, name='delete_teacher'),
]
