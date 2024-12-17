from rest_framework import serializers
from api.models import (User, Course, CourseSection, CourseBatch, Question, QuestionOption, AnswerOption, Exam, ExamQuestion, 
                        Student, StudentCourse, StudentExam, StudentExamQuestion, StudentExamAnswer)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class CourseSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseSection
        fields = '__all__'

class CourseBatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseBatch
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class QuestionOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionOption
        fields = '__all__'

class AnswerOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerOption
        fields = '__all__'

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'

class ExamQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamQuestion
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class StudentCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentCourse
        fields = '__all__'

class StudentExamQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentExamQuestion
        fields = '__all__'

class StudentExamAnswerSerializer(serializers.ModelSerializer):
    # class Meta:
    #     model = StudentExamAnswer
    #     fields = '__all__'
    class Meta:
        model = StudentExamAnswer
        fields = ['id', 'student_answer', 'is_correct', 'question_id']
        extra_kwargs = {
            'id': {'read_only': True}  # Make `id` field read-only
        }

class StudentExamSerializer(serializers.ModelSerializer):
    # class Meta:
    #     model = StudentExam
    #     fields = '__all__'
    qanswers = StudentExamAnswerSerializer(many=True, write_only=True)
    
    class Meta:
        model = StudentExam
        fields = [
            'id', 'exam_start_date_time', 'exam_end_date_time', 'result',
            'no_of_questions', 'no_of_correct_answers', 'exam_id',
            'student_id', 'qanswers'
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