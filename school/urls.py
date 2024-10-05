from django.urls import path
from .views import (StudentCreateView, HomePageView, StudentListView, StudentDetailView, StudentUpdateView,
                    StudentDeleteView, TeacherCreateView, TeacherListView, TeacherDetailView, TeacherUpdateView,
                    TeacherDeleteView, SubjectCreateView, SubjectListView, SubjectDetailView, SubjectUpdateView,
                    SubjectDeleteView)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    # urls for Student
    path('student_create/', StudentCreateView.as_view(), name='student_create'),
    path('student_list/', StudentListView.as_view(), name='student_list'),
    path('student_detail/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    path('student_update/<int:pk>/', StudentUpdateView.as_view(), name='student_update'),
    path('student_delete/<int:pk>/', StudentDeleteView.as_view(), name='student_delete'),
    # urls for Teacher
    path('teacher_add/', TeacherCreateView.as_view(), name='teacher_create'),
    path('teacher_list/', TeacherListView.as_view(), name='teachers_list'),
    path('teacher_detail/<int:pk>/', TeacherDetailView.as_view(), name='teacher_detail'),
    path('teacher_update/<int:pk>/', TeacherUpdateView.as_view(), name='teacher_update'),
    path('teacher_delete/<int:pk>/', TeacherDeleteView.as_view(), name='teacher_delete'),
    # urls for Subject
    path('subject_create/', SubjectCreateView.as_view(), name='subject_create'),
    path('subject_list/', SubjectListView.as_view(), name='subject_list'),
    path('subject_detail/<int:pk>/', SubjectDetailView.as_view(), name='subject_detail'),
    path('subject_update/<int:pk>/', SubjectUpdateView.as_view(), name='subject_update'),
    path('subject_delete/<int:pk>/', SubjectDeleteView.as_view(), name='subject_delete'),



]

