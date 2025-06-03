from rest_framework import serializers
from app.modules.general_module.serializers.base_serializer import BaseModelSerializer
from app.modules.exam_management.models.question_option import QuestionOption

class QuestionOptionSerializer(BaseModelSerializer,serializers.ModelSerializer):
    class Meta:
        model = QuestionOption
        fields = '__all__'