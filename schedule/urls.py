from django.urls import path
from .views import MainPageView, CoursePageView, TeacherPageView, AddCourseView, SignUpView, LoginView, LogoutView
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='schedule-main')),
    path('schedule/main/', MainPageView.as_view(), name="schedule-main"),
    path('schedule/course_details/<int:course_id>/', CoursePageView.as_view(), name="course-details"),
    path('schedule/teacher_details/<int:teacher_id>/', TeacherPageView.as_view(), name="teacher-details"),
    path('schedule/add_course/', AddCourseView.as_view(), name="add-course"),
    path('signup/', SignUpView.as_view(), name="signup"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
]