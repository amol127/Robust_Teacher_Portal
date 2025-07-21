from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('student/add/', views.add_student, name='add_student'),
    path('student/edit/<int:student_id>/', views.edit_student, name='edit_student'),
    path('student/delete/<int:student_id>/', views.delete_student, name='delete_student'),
] 