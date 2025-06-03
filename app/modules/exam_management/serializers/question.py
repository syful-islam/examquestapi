from rest_framework import serializers
from app.modules.general_module.serializers.base_serializer import BaseModelSerializer
from app.modules.exam_management.models.question import Question

class QuestionSerializer(BaseModelSerializer,serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'