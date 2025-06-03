from rest_framework import serializers
from app.modules.general_module.serializers.base_serializer import BaseModelSerializer
from app.modules.student_management.models.student import Student

class StudentSerializer(BaseModelSerializer,serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'