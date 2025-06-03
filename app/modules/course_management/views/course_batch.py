from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from app.core.mixins import AutoSetSubscriberMixin
from app.modules.course_management.models.course_batch import CourseBatch
from app.modules.course_management.serializers.course_batch import CourseBatchSerializer

class CourseBatchViewSet(AutoSetSubscriberMixin,viewsets.ModelViewSet):
    queryset = CourseBatch.objects.all()
    serializer_class = CourseBatchSerializer

    def get_serializer_class(self):
        if self.action in ['retrieve']:  # For GET requests
            return CourseBatchSerializer
        return CourseBatchSerializer  # For POST/PUT requests
    
    def get_queryset(self):
        return super().get_queryset()
from app.modules.course_management.serializers.course_batch import CourseBatchSerializer

# @api_view(['GET'])
# def get_course_batches(request):
#     batches = CourseBatch.objects.all()
#     serializer = CourseBatchSerializer(batches, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def create_course_batch(request):
#     serializer = CourseBatchSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def course_batch_detail(request, pk):
#     try:
#         batch = CourseBatch.objects.get(pk=pk)
#     except CourseBatch.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = CourseBatchSerializer(batch)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = CourseBatchSerializer(batch, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         batch.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)