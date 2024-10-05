from django.urls import path
from .views import (StudentCreateView, HomePageView, StudentListView, StudentDetailView, StudentUpdateView,
                    StudentDeleteView, TeacherCreateView, TeacherListView, TeacherDetailView, TeacherUpdateView,
                    TeacherDeleteView)
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('student_create/', StudentCreateView.as_view(), name='student_create'),
    path('student_list/', StudentListView.as_view(), name='student_list'),
    path('student_detail/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    path('student_update/<int:pk>/', StudentUpdateView.as_view(), name='student_update'),
    path('student_delete/<int:pk>/', StudentDeleteView.as_view(), name='student_delete'),
    path('teacher_add/', TeacherCreateView.as_view(), name='teacher_create'),
    path('teacher_list/', TeacherListView.as_view(), name='teachers_list'),
    path('teacher_detail/<int:pk>/', TeacherDetailView.as_view(), name='teacher_detail'),
    path('teacher_update/<int:pk>/', TeacherUpdateView.as_view(), name='teacher_update'),
    path('teacher_delete/<int:pk>/', TeacherDeleteView.as_view(), name='teacher_delete'),


]

