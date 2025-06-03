from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from app.modules.student_management.models import CourseSection
from app.modules.student_management.serializers.serializer import CourseSectionSerializer

@api_view(['GET'])
def get_course_sections(request):
    sections = CourseSection.objects.all()
    serializer = CourseSectionSerializer(sections, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_course_section(request):
    serializer = CourseSectionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def course_section_detail(request, pk):
    try:
        section = CourseSection.objects.get(pk=pk)
    except CourseSection.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CourseSectionSerializer(section)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CourseSectionSerializer(section, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        section.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)