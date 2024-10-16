from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:todo_id>/', views.delete, name='delete'),
    path('delete_multiple/', views.delete_multiple, name='delete_multiple'),
]