from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from app.core.mixins import AutoSetSubscriberMixin
from app.modules.exam_management.models.question_option import QuestionOption
from app.modules.exam_management.serializers.question_option import QuestionOptionSerializer

class QuestionOptionViewSet(AutoSetSubscriberMixin,viewsets.ModelViewSet):
    queryset = QuestionOption.objects.all()
    serializer_class = QuestionOptionSerializer

    def get_serializer_class(self):
        if self.action in ['retrieve']:  # For GET requests
            return QuestionOptionSerializer
        return QuestionOptionSerializer  # For POST/PUT requests
    
    def get_queryset(self):
        return super().get_queryset()

# @api_view(['GET'])
# def get_question_options(request):
#     options = QuestionOption.objects.all()
#     serializer = QuestionOptionSerializer(options, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def create_question_option(request):
#     serializer = QuestionOptionSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def question_option_detail(request, pk):
#     try:
#         option = QuestionOption.objects.get(pk=pk)
#     except QuestionOption.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = QuestionOptionSerializer(option)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = QuestionOptionSerializer(option, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         option.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)