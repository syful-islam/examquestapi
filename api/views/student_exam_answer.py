from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from api.models import StudentExamAnswer
from api.serializer import StudentExamAnswerSerializer

@api_view(['GET'])
def get_student_exam_answers(request):
    answers = StudentExamAnswer.objects.all()
    serializer = StudentExamAnswerSerializer(answers, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_student_exam_answer(request):
    serializer = StudentExamAnswerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def student_exam_answer_detail(request, pk):
    try:
        answer = StudentExamAnswer.objects.get(pk=pk)
    except StudentExamAnswer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentExamAnswerSerializer(answer)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StudentExamAnswerSerializer(answer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        answer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)