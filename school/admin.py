from django.contrib import admin

from .models import Student, Teacher, Class, Subject


@admin.register(Teacher)
class Teacher(admin.ModelAdmin):
    list_display = ['name', 'subject']
    search_fields = ['name', 'subject']
    list_filter = ['name', 'subject']


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'teacher']
    search_fields = ['name', 'teacher']
    list_filter = ['name', 'teacher']


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name', 'teacher', 'subject']
    list_filter = ['teacher', 'subject']


@admin.register(Student)
class Student(admin.ModelAdmin):
    list_display = ['name', 'roll_no', 'email', 'status']
    search_fields = ['name', 'roll_no', 'class_name', 'email']
    list_filter = ['class_name', 'status']
