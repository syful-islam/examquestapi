from rest_framework import serializers
from app.modules.general_module.serializers.base_serializer import BaseModelSerializer
from app.modules.course_management.models.course_batch import CourseBatch

class CourseBatchSerializer(BaseModelSerializer,serializers.ModelSerializer):
    class Meta:
        model = CourseBatch
        fields = '__all__'