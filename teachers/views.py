from django.shortcuts import render

# Create your views here.


def get_all_teacher(request):
    return render(request, 'teachers/teachers.html')