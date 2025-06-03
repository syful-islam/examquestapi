from rest_framework import serializers
from app.modules.general_module.serializers.base_serializer import BaseModelSerializer
from app.modules.course_management.models.course_section import CourseSection

class CourseSectionSerializer(BaseModelSerializer,serializers.ModelSerializer):
    class Meta:
        model = CourseSection
        fields = '__all__'