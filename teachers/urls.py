from django.urls import path

from . import views

app_name = 'teachers'

urlpatterns = [
    path('', views.get_all_teacher, name='teachers'),
]