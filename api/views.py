from rest_framework.response import Response
from rest_framework.views import APIView
from student.models import Student
from .serializers import StudentSerializer


class StudentListView (APIView):
    def get (self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(student, many = True)
        return Response(serializer.data)
