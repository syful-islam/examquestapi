from django.db import models
from .course import Course

class CourseSection(models.Model):
    section_id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='chapters')
    chapter_no = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='sections')
    section_no = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='subsections')
    subsection_no = models.CharField(max_length=100)
    section_name = models.CharField(max_length=100)

    def __str__(self):
        return self.section_name