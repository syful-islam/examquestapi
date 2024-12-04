from django.db import models
import json
from .student import Student
from .exam import Exam
from .question import Question

class StudentExamQuestion(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    question_serial_no = models.IntegerField()
    question_text = models.TextField()
    question_type = models.CharField(max_length=50)
    options = models.JSONField()
    answers = models.JSONField()
    is_correct = models.BooleanField()

    def __str__(self):
        options_str = json.dumps(self.options)
        answers_str = json.dumps(self.answers)
        return f"{self.id} - {self.question_serial_no} - {self.question_text} - {self.question_type} - Options: {options_str} - Answers: {answers_str}"