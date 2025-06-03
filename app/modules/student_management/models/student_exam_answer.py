from django.db import models
from app.modules.general_module.models.base_model import BaseModel
from .student import Student
from app.modules.exam_management.models.exam import Exam
from app.modules.exam_management.models.question import Question

class StudentExamAnswer(BaseModel):
    # student = models.ForeignKey(Student, on_delete=models.CASCADE)
    # exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    # question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # student_answer = models.JSONField()
    # is_correct = models.BooleanField()

    # def __str__(self):
    #     return f"{self.student.student_name} - {self.exam.exam_name} - {self.question.question_text}"
    exam_id = models.IntegerField(default=1)
    student_id = models.IntegerField(default=1)
    question_id = models.IntegerField(default=1)
    student_answer = models.JSONField()
    is_correct = models.BooleanField()    
    
    class Meta:
        db_table = "api_studentexamanswer"