from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)

    def __str__(self):
        return f" Teacher: {self.name} - Specialized in : {self.subject}"


class Subject(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='subjects')

    def __str__(self):
        return f" Subject : {self.name}  Taught by : {self.teacher.name}"


class Class(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='classes')
    subject = models.ManyToManyField(Subject, related_name='classes')

    class Meta:
        verbose_name_plural = 'classes'

    def __str__(self):
        return f" Class : {self.name} - Assigned to : {self.teacher.name} - Specialized in: {self.teacher.subject}"


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField(unique=True)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='students')
    subject = models.ManyToManyField(Subject, related_name='students')
    email = models.EmailField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('graduated', 'Graduated'), ('transferred', 'Transferred')]
                              , default='active', null=True)

    def __str__(self):
        return f" Student: {self.name} Roll_no: {self.roll_no} Class: {self.class_name.name}"
