# from django.contrib import admin
from django.urls import path, include
# from .views import StudentListView
# from django.urls import include
from api.views import StudentListView,TeacherListView, CourseListView


urlpatterns = [
    path("students/", StudentListView.as_view(), name="student_list_view"),
    path("course/", CourseListView.as_view(), name="course_list_view"),
    path("teacher/", TeacherListView.as_view(), name="teacher_list_view"),
    path("classperiod/", ClassPeriodListView.as_view(), name="classperiod_list_view"),
    path('app_name/', include('app_name.urls')),
]

