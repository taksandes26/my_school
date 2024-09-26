from django.urls import path
from .views import home, student_list, teacher_list, class_list, subject_list

urlpatterns = [
    path('home/', home, name='home'),
    path('student_list/', student_list, name='student_list'),
    path('teachers_list/', teacher_list, name='teacher_list'),
    path('classes/', class_list, name='class_list'),
    path('subjects/', subject_list, name='subject_list'),
]

