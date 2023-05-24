from django.db import models
from django.urls import reverse


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()
    about = models.TextField()

    def __str__(self):
        return f'Teacher: {self.name} {self.surname}'

    def get_absolute_url(self):
        return reverse('teacher-details', kwargs={'id': self.id})


class Course(models.Model):
    title = models.CharField(max_length=255)
    info = models.TextField()
    duration_months = models.IntegerField()
    price = models.IntegerField()
    teacher = models.ManyToManyField(Teacher, related_name='courses')

    def __str__(self):
        return f'Course: {self.title}'

    def get_absolute_url(self):
        return reverse('course-details', kwargs={'id': self.id})


class Student(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()
    course = models.ManyToManyField(Course, related_name='students')

    def __str__(self):
        return f'Student: {self.name} {self.surname}'
