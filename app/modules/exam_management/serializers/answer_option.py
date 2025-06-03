from rest_framework import serializers
from app.modules.general_module.serializers.base_serializer import BaseModelSerializer
from app.modules.exam_management.models.answer_option import AnswerOption

class AnswerOptionSerializer(BaseModelSerializer,serializers.ModelSerializer):
    class Meta:
        model = AnswerOption
        fields = '__all__'