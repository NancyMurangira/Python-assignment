from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from student.models import Student
from teacher.models import Teacher
from student.models import Student
from ClassPeriod.models import ClassPeriod
from .serializers import StudentSerializer, TeacherSerializer, CourseSerializer


class StudentListView(APIView):
    def get (self, request):
        students = Students.objects.all()
        serializer = StudentSerializer(students, many = True)
        return Response(serializer.data)
    
class CourseListView (APIView):
    def get (self, request):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many= True)
        return Response (serializer.data)

class TeacherListView(APIView):
    def get(self, request):
        teacher = Teacher.objects.all()
        serializer = TeacherSerializer(teacher,many= True)
        return Response (serializer.data)

class ClassPeriodListView(APIView):
    def get (self, request):
        classperiod = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(teacher, many= True)
        return Response (serializer.data)

