from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from app.core.mixins import AutoSetSubscriberMixin
from app.modules.exam_management.models.question import Question
from app.modules.exam_management.serializers.question import QuestionSerializer

class QuestionViewSet(AutoSetSubscriberMixin,viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get_serializer_class(self):
        if self.action in ['retrieve']:  # For GET requests
            return QuestionSerializer
        return QuestionSerializer  # For POST/PUT requests
    
    def get_queryset(self):
        return super().get_queryset()

# @api_view(['GET'])
# def get_questions(request):
#     questions = Question.objects.all()
#     serializer = QuestionSerializer(questions, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def create_question(request):
#     serializer = QuestionSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def question_detail(request, pk):
#     try:
#         question = Question.objects.get(pk=pk)
#     except Question.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = QuestionSerializer(question)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = QuestionSerializer(question, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         question.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)