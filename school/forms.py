from django import forms
from .models import Student, Teacher, Class, Subject


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['id', 'name', 'subject']


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['id', 'name', 'teacher']


class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['id', 'name', 'teacher', 'subject']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll_no', 'class_name', 'subject', 'email', 'status']
