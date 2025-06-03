from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from app.core.mixins import AutoSetSubscriberMixin
from app.modules.course_management.models.course import Course
from app.modules.course_management.serializers.course import CourseSerializer

class CourseViewSet(AutoSetSubscriberMixin,viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_serializer_class(self):
        if self.action in ['retrieve']:  # For GET requests
            return CourseSerializer
        return CourseSerializer  # For POST/PUT requests
    
    def get_queryset(self):
        return super().get_queryset()

# @api_view(['GET'])
# def get_courses(request):
#     courses = Course.objects.all()
#     serializer = CourseSerializer(courses, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def create_course(request):
#     serializer = CourseSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def course_detail(request, pk):
#     try:
#         course = Course.objects.get(pk=pk)
#     except Course.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = CourseSerializer(course)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = CourseSerializer(course, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         course.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)