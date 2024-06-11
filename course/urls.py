from django.urls import path
from . import views

urlpatterns = [
	path('', views.course_list, name='course_list'),
	path('new/', views.create_course, name='create_course'),
	path('delete/<int:course_id>/', views.delete_course, name='delete_course'),
]