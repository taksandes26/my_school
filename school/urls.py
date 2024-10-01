from django.urls import path
from .views import StudentCreateView, HomePageView, StudentListView, StudentDetailView, StudentUpdateView, StudentDeleteView
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('student_create/', StudentCreateView.as_view(), name='student_create'),
    path('student_list/', StudentListView.as_view(), name='student_list'),
    path('student_detail/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    path('student_update/<int:pk>/', StudentUpdateView.as_view(), name='student_update'),
    path('student_delete/<int:pk>/', StudentDeleteView.as_view(), name='student_delete'),
    # path('about-us/', about_us, name='about_us'),
    # path('contact-us/', contact_us, name='contact_us'),
    # path('privacy-policy/', privacy_policy, name='privacy_policy'),

]

