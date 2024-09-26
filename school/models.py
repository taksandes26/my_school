# from django.db import models
#
#
# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     std = models.CharField(max_length=10)
#
#     def __str__(self):
#         return self.name
#
#
# class Teacher(models.Model):
#     name = models.CharField(max_length=100)
#     subject = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.name
#
#
# class Class(models.Model):
#     name = models.CharField(max_length=10)
#     teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='classes')
#
#     def __str__(self):
#         return self.teacher
#
#
# class Subject(models.Model):
#     name = models.CharField(max_length=100)
#     teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='subjects')
#     class_name = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='classes')
#
#     def __str__(self):
#         return self.name
