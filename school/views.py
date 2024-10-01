from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from .models import Student
from .forms import StudentForm


class HomePageView(View):
    def get(self, request):
        return render(request, 'school/home.html')


class StudentCreateView(View):
    form_class = StudentForm
    initial_template = 'school/students.html'
    template_name = 'school/student_created.html'

    def get(self, request):
        user_form = self.form_class
        return render(request, self.initial_template, {'user_form': user_form})

    def post(self, request):
        user_form = self.form_class(request.POST)
        if user_form.is_valid():
            new_student = user_form.save()
            return render(request, self.template_name, {'new_student': new_student})
        else:
            return render(request, self.initial_template, {'user_form': user_form})


class StudentListView(View):
    def get(self, request):
        student = Student.objects.all()
        return render(request, 'school/student_list.html', {'student': student})


class StudentDetailView(View):
    def get(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        return render(request, 'school/student_detail.html', {'student': student})


class StudentUpdateView(View):
    form_class = StudentForm
    template_name = 'school/student_update.html'

    def get(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        user_form = self.form_class(instance=student)
        return render(request, self.template_name, {'user_form': user_form, 'student': student})

    def post(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        user_form = self.form_class(request.POST, instance=student)
        if user_form.is_valid():
            updated_data = user_form.save()
            print("saved successfully")
            return redirect('student_list')
        return render(request, self.template_name, {'user_form': user_form, 'student': student})


class StudentDeleteView(View):

    def get(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        return render(request, 'school/student_delete.html', {'student': student})

    def post(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        student.delete()
        return redirect('student_list')





# def teacher_list(request):
#     teachers_list = [
#         {'id': 1, 'name': 'Johnson', 'subject': 'Mathematics'},
#         {'id': 2, 'name': ' David', 'subject': 'Science'},
#         {'id': 3, 'name': ' sam', 'subject': 'Geography'},
#
#     ]
#     return render(request, 'school/teachers.html', {'teachers': teachers_list})
#
#
# def class_list(request):
#     classes_list = [
#         {'name': '2A'},
#         {'name': '5A'},
#         {'name': '9A'},
#
#     ]
#     return render(request, 'school/classes.html', {'classes': classes_list})
#
#
# def subject_list(request):
#     subjects_list = [
#         {'id': 1, 'name': 'Mathematics'},
#         {'id': 2, 'name': 'Science'},
#         {'id': 3, 'name': 'Geography'},
#
#     ]
#     return render(request, 'school/subjects.html', {'subjects': subjects_list})
#
#
# def about_us(request):
#     return render(request, 'school/about_us.html')
#
#
# def contact_us(request):
#     return render(request, 'school/contact_us.html')
#
#
# def privacy_policy(request):
#     return render(request, 'school/privacy_policy.html')
