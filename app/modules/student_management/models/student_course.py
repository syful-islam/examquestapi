from django.db import models
from app.modules.general_module.models.base_model import BaseModel
from .student import Student
from app.modules.course_management.models.course import Course
from app.modules.course_management.models.course_batch import CourseBatch

class StudentCourse(BaseModel):
    # enrollment_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    batch = models.ForeignKey(CourseBatch, on_delete=models.CASCADE)
    enrollment_date = models.DateField()
    enrollment_serial = models.IntegerField()

    def __str__(self):
        return f"{self.student.student_name} - {self.course.course_name}"