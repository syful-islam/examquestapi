from rest_framework import serializers
from app.modules.general_module.serializers.base_serializer import BaseModelSerializer
from app.modules.course_management.models.course import Course

class CourseSerializer(BaseModelSerializer,serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'