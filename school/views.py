from django.shortcuts import render


def home(request):
    return render(request, 'school/home.html')


def student_list(request):
    students_list = [
        {'id': 1, 'name': 'raj', 'roll_no': 13, 'class': '5A'},
        {'id': 2, 'name': 'shlok', 'roll_no': 27, 'class': '4A'},
        {'id': 3, 'name': 'varun', 'roll_no': 33, 'class': '10A'},
    ]

    return render(request, 'school/students.html', {'students': students_list})


def teacher_list(request):
    teachers_list = [
        {'id': 1, 'name': 'Johnson', 'subject': 'Mathematics'},
        {'id': 2, 'name': ' David', 'subject': 'Science'},
        {'id': 3, 'name': ' sam', 'subject': 'Geography'},

    ]
    return render(request, 'school/teachers.html', {'teachers': teachers_list})


def class_list(request):
    classes_list = [
        {'id': 1, 'name': '2A'},
        {'id': 2, 'name': '5A'},
        {'id': 3, 'name': '9A'},

    ]
    return render(request, 'school/classes.html', {'classes': classes_list})


def subject_list(request):
    subjects_list = [
        {'id': 1, 'name': 'Mathematics'},
        {'id': 2, 'name': 'Science'},
        {'id': 3, 'name': 'Geography'},

    ]
    return render(request, 'school/subjects.html', {'subjects': subjects_list})
