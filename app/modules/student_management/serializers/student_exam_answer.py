from rest_framework import serializers
from app.modules.general_module.serializers.base_serializer import BaseModelSerializer
from app.modules.student_management.models.student_exam_answer import StudentExamAnswer

class StudentExamAnswerSerializer(BaseModelSerializer,serializers.ModelSerializer):
    class Meta:
        model = StudentExamAnswer
        fields = ['id', 'student_answer', 'is_correct', 'question_id']
        extra_kwargs = {
            'id': {'read_only': True}  # Make `id` field read-only
        }

