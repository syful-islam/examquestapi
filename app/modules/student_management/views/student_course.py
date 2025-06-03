from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from app.modules.student_management.models import StudentCourse
from app.modules.student_management.serializers.serializer import StudentCourseSerializer

@api_view(['GET'])
def get_student_courses(request, studentId):
    student_courses = StudentCourse.objects.get(studentId=studentId)
    serializer = StudentCourseSerializer(student_courses, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_student_course(request):
    serializer = StudentCourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def student_course_detail(request, pk):
    try:
        student_course = StudentCourse.objects.get(pk=pk)
    except StudentCourse.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentCourseSerializer(student_course)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StudentCourseSerializer(student_course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student_course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)