from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.index, name='index'),
    path('<int:id>/', views.view_student, name='view_student'),
    path('add/', views.add, name='add'), 
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),  
]
