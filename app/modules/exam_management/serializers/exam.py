from rest_framework import serializers
from app.modules.general_module.serializers.base_serializer import BaseModelSerializer
from app.modules.exam_management.models.exam import Exam

class ExamSerializer(BaseModelSerializer,serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'