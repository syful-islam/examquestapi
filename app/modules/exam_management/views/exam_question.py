from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from app.core.mixins import AutoSetSubscriberMixin
from app.modules.exam_management.models.exam_question import ExamQuestion
from app.modules.exam_management.serializers.exam_question import ExamQuestionSerializer

class ExamQuestionViewSet(AutoSetSubscriberMixin,viewsets.ModelViewSet):
    queryset = ExamQuestion.objects.all()
    serializer_class = ExamQuestionSerializer

    def get_serializer_class(self):
        if self.action in ['retrieve']:  # For GET requests
            return ExamQuestionSerializer
        return ExamQuestionSerializer  # For POST/PUT requests
    
    def get_queryset(self):
        return super().get_queryset()

# @api_view(['GET'])
# def get_exam_questions(request):
#     exam_questions = ExamQuestion.objects.all()
#     serializer = ExamQuestionSerializer(exam_questions, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def create_exam_question(request):
#     serializer = ExamQuestionSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def exam_question_detail(request, pk):
#     try:
#         exam_question = ExamQuestion.objects.get(pk=pk)
#     except ExamQuestion.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = ExamQuestionSerializer(exam_question)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = ExamQuestionSerializer(exam_question, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         exam_question.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)