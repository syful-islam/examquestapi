from rest_framework import serializers
from app.modules.general_module.serializers.base_serializer import BaseModelSerializer
from app.modules.exam_management.models.exam_question import ExamQuestion

class ExamQuestionSerializer(BaseModelSerializer,serializers.ModelSerializer):
    class Meta:
        model = ExamQuestion
        fields = '__all__'