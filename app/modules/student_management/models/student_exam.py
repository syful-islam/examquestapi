from django.db import models
from django.utils import timezone
from .student import Student
from .exam import Exam

class StudentExam(models.Model):
    # student = models.ForeignKey(Student, on_delete=models.CASCADE)
    # exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    # exam_start_date_time = models.DateTimeField()
    # exam_end_date_time = models.DateTimeField()
    # result = models.CharField(max_length=10)  # Pass/Fail
    # no_of_questions = models.IntegerField()
    # no_of_correct_answers = models.IntegerField()

    # def __str__(self):
    #     return f"{self.student.student_name} - {self.exam.exam_name}"
    exam_id = models.IntegerField(default=1)
    student_id = models.IntegerField(default=1)
    exam_start_date_time = models.DateTimeField(null=True, blank=True)
    exam_end_date_time = models.DateTimeField(null=True, blank=True)
    result = models.CharField(max_length=10,null=True, blank=True)
    no_of_questions = models.IntegerField(null=True, blank=True)
    no_of_correct_answers = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "api_studentexam"