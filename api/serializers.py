from rest_framework import serializers
from student.models import Student
from course.models import Course
from student.models import Student
from teacher.models import Teacher
from ClassPeriod.models import ClassPeriodConfig


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields="__all__"
    class TeacherSerializer(serializers.ModelSerializer):
        class Meta:
            model=Teacher
            fields ="__all__"
    class CourseSerializer(serializers.ModelSerializer):
        class Meta:
            model = Course
            fields = "__all__"

        class ClassPeriodSerializer(serializers.ModelSerializer):
            class Meta:
                model = ClassPeriodConfig
                fields = "__all__"
