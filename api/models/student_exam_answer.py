from django.db import models
from .student import Student
from .exam import Exam
from .question import Question

class StudentExamAnswer(models.Model):
    # student = models.ForeignKey(Student, on_delete=models.CASCADE)
    # exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    # question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # student_answer = models.JSONField()
    # is_correct = models.BooleanField()

    # def __str__(self):
    #     return f"{self.student.student_name} - {self.exam.exam_name} - {self.question.question_text}"
    exam_id = models.IntegerField()
    student_id = models.IntegerField()
    question_id = models.IntegerField()
    student_answer = models.JSONField()
    is_correct = models.BooleanField()    
    
    class Meta:
        db_table = "api_studentexamanswer"