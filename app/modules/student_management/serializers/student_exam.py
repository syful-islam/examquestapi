from rest_framework import serializers
from app.modules.general_module.serializers.base_serializer import BaseModelSerializer
from app.modules.student_management.models.student_exam import StudentExam
from app.modules.student_management.models.student_exam_answer import StudentExamAnswer
from app.modules.student_management.serializers.student_exam_answer import StudentExamAnswerSerializer

class StudentExamInitSerializer(BaseModelSerializer,serializers.ModelSerializer):
    class Meta:
        model = StudentExam
        fields = [
            'id', 'exam_id', 'student_id','exam_start_date_time'
        ]

class StudentExamSerializer(BaseModelSerializer,serializers.ModelSerializer):
    class Meta:
        model = StudentExam
        fields = '__all__'

class StudentExamSubmitSerializer(BaseModelSerializer,serializers.ModelSerializer):
    qanswers = StudentExamAnswerSerializer(many=True, write_only=True)
    
    class Meta:
        model = StudentExam
        fields = [
            'id', 'exam_end_date_time','result',
            'no_of_questions', 'no_of_correct_answers', 'qanswers'
        ]
    
    def create(self, validated_data):
        qanswers_data = validated_data.pop('qanswers')
        student_exam = StudentExam.objects.create(**validated_data)

        # Create answers and link to the current StudentExam
        for answer_data in qanswers_data:
            StudentExamAnswer.objects.create(
                student_answer=answer_data['student_answer'],
                is_correct=answer_data['is_correct'],
                question_id=answer_data['question_id'],
                exam_id=validated_data['exam_id'],  # Inherit exam_id
                student_id=validated_data['student_id']  # Inherit student_id
            )
        return student_exam