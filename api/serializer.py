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

class StudentExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentExam
        fields = '__all__'

class StudentExamQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentExamQuestion
        fields = '__all__'

class StudentExamAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentExamAnswer
        fields = '__all__'