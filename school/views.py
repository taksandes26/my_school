from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from .models import Student, Teacher, Subject, Class
from .forms import StudentForm, TeacherForm, SubjectForm, ClassForm


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
        user_form = self.form_class(data=request.POST, instance=student)
        if user_form.is_valid():
            user_form.save()
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


class TeacherCreateView(View):
    form_class = TeacherForm
    initial_template = 'school/teacher.html'
    template_name = 'school/teacher_create.html'

    def get(self, request):
        teacher_form = self.form_class()
        return render(request, self.initial_template, {'teacher_form': teacher_form})

    def post(self, request):
        teacher_form = self.form_class(request.POST)
        if teacher_form.is_valid():
            teacher = teacher_form.save()
            return render(request, self.template_name, {'teacher': teacher})
        else:
            return render(request, self.initial_template, {'teacher_form': teacher_form})


class TeacherListView(View):
    def get(self, request):
        teachers = Teacher.objects.all()
        return render(request, 'school/teacher_list.html', {'teachers': teachers})


class TeacherDetailView(View):
    def get(self, request, pk):
        teacher = get_object_or_404(Teacher, pk=pk)
        return render(request, 'school/teacher_detail.html', {'teacher': teacher})


class TeacherUpdateView(View):
    form_class = TeacherForm
    template_name = 'school/teacher_update.html'

    def get(self, request, pk):
        teacher = get_object_or_404(Teacher, pk=pk)
        teacher_form = self.form_class(instance=teacher)
        return render(request, self.template_name, {'teacher_form': teacher_form, 'teacher': teacher})

    def post(self, request, pk):
        teacher = get_object_or_404(Teacher, pk=pk)
        teacher_form = self.form_class(data=request.POST, instance=teacher)
        if teacher_form.is_valid():
            teacher_form.save()
            return redirect('teachers_list')
        else:
            teacher_form = self.form_class
            return render(request, self.template_name, {'teacher_form': teacher_form, 'teacher': teacher})


class TeacherDeleteView(View):
    def get(self, request, pk):
        teacher = get_object_or_404(Teacher, pk=pk)
        return render(request, 'school/teacher_delete.html', {'teacher': teacher})

    def post(self, request, pk):
        teacher = get_object_or_404(Teacher, pk=pk)
        teacher.delete()
        return redirect('teachers_list')


class SubjectCreateView(View):
    form_class = SubjectForm
    initial_template = 'school/subject.html'
    template_name = 'school/subject_create.html'

    def get(self, request):
        subject_form = self.form_class
        return render(request, self.initial_template, {'subject_form': subject_form})

    def post(self, request):
        subject_form = self.form_class(request.POST)
        if subject_form.is_valid():
            subject_form.save()
            return render(request, self.template_name, {'subject_form': subject_form})
        else:
            return render(request, self.initial_template, {'subject_form': subject_form})
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
