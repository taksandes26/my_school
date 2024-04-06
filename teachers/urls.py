from django.urls import path
from . import views

urlpatterns = [
    path('', views.teachers, name='home'),
    path('teachers/', views.teachers, name='home'),

]
