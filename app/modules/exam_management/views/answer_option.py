from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from app.core.mixins import AutoSetSubscriberMixin
from app.modules.exam_management.models.answer_option import AnswerOption
from app.modules.exam_management.serializers.answer_option import AnswerOptionSerializer

class AnswerOptionViewSet(AutoSetSubscriberMixin,viewsets.ModelViewSet):
    queryset = AnswerOption.objects.all()
    serializer_class = AnswerOptionSerializer

    def get_serializer_class(self):
        if self.action in ['retrieve']:  # For GET requests
            return AnswerOptionSerializer
        return AnswerOptionSerializer  # For POST/PUT requests
    
    def get_queryset(self):
        return super().get_queryset()

# @api_view(['GET'])
# def get_answer_options(request):
#     options = AnswerOption.objects.all()
#     serializer = AnswerOptionSerializer(options, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def create_answer_option(request):
#     serializer = AnswerOptionSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def answer_option_detail(request, pk):
#     try:
#         option = AnswerOption.objects.get(pk=pk)
#     except AnswerOption.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = AnswerOptionSerializer(option)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = AnswerOptionSerializer(option, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         option.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)