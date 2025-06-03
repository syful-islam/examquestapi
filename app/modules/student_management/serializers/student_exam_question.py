from rest_framework import serializers
from app.modules.general_module.serializers.base_serializer import BaseModelSerializer
from app.modules.student_management.models.student_exam_question import StudentExamQuestion

class StudentExamQuestionSerializer(BaseModelSerializer,serializers.ModelSerializer):
    class Meta:
        model = StudentExamQuestion
        fields = '__all__'