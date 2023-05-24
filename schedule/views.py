from django.forms import models
from django.shortcuts import render, redirect
from .forms import StudentForm, SearchForm, LoginForm
from .models import Course, Student, Teacher
from django.views import View
from django.http import Http404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, DetailView

from . import models

# Create your views here.
class MainPageView(View):
    def get(self, request, *args, **kwargs):
        q = request.GET.get('q')
        if q:
            # if the user has searched for something
            courses = Course.objects.filter(title__contains=q)
        else:

            # display all courses
            courses = Course.objects.all()

        return render(request, 'schedule/index.html', {'courses': courses})


class CoursePageView(DetailView):
    def get(self, request, *args, **kwargs):
        try:
            course_id = kwargs.get('course_id')
            course = Course.objects.get(pk=course_id)
        except Course.DoesNotExist:
            raise Http404
        return render(request, 'schedule/course_details.html', {'course': course})


class TeacherPageView(DetailView):
    def get(self, request, *args, **kwargs):
        teacher_id = kwargs.get('teacher_id')
        teacher = Teacher.objects.get(pk=teacher_id)
        return render(request, 'schedule/teacher_details.html', {'teacher': teacher})


class StudentPageView(View):
    def get(self, request, *args, **kwargs):
        student_id = kwargs.get('student_id')
        student = Student.objects.get(pk=student_id)
        return render(request, 'schedule/student_details.html', {'student': student})


class AddCourseView(View):
    def get(self, request, *args, **kwargs):
        form = StudentForm()
        return render(request, 'schedule/add_course.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/schedule/add_course')


class SignUpView(CreateView):
    def get(self, request, *args, **kwargs):
        form = UserCreationForm()
        return render(request, 'schedule/signup.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/schedule/main')


class LoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'schedule/login.html'

    def form_valid(self, form):
        login(self.request, form.get_user())
        return redirect('/schedule/main')

class LogoutView(LogoutView):
    next_page = '/schedule/main'