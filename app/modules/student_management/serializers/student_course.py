from rest_framework import serializers
from app.modules.general_module.serializers.base_serializer import BaseModelSerializer
from app.modules.student_management.models.student_course import StudentCourse

class StudentCourseSerializer(BaseModelSerializer,serializers.ModelSerializer):
    class Meta:
        model = StudentCourse
        fields = '__all__'
