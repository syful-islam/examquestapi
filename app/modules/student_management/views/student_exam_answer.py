from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from app.core.mixins import AutoSetSubscriberMixin
from app.modules.student_management.models.student_exam_answer import StudentExamAnswer
from app.modules.student_management.serializers.student_exam_answer import StudentExamAnswerSerializer

class StudentExamAnswerViewSet(AutoSetSubscriberMixin,viewsets.ModelViewSet):
    queryset = StudentExamAnswer.objects.all()
    serializer_class = StudentExamAnswerSerializer

    def get_serializer_class(self):
        if self.action in ['retrieve']:  # For GET requests
            return StudentExamAnswerSerializer
        return StudentExamAnswerSerializer  # For POST/PUT requests
    
    def get_queryset(self):
        return super().get_queryset()

# @api_view(['GET'])
# def get_student_exam_answers(request):
#     answers = StudentExamAnswer.objects.all()
#     serializer = StudentExamAnswerSerializer(answers, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def create_student_exam_answer(request):
#     serializer = StudentExamAnswerSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def student_exam_answer_detail(request, pk):
#     try:
#         answer = StudentExamAnswer.objects.get(pk=pk)
#     except StudentExamAnswer.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = StudentExamAnswerSerializer(answer)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = StudentExamAnswerSerializer(answer, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         answer.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)