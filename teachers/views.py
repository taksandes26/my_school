from django.shortcuts import render
from django.http import HttpResponse
from .models import Teachers


# Create your views here.
def teachers(request):
    Teachers.objects.all()
    return render(request, "teachers.html")
