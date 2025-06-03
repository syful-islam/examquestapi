from django.db import models
from .exam import Exam
from .question import Question

class ExamQuestion(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    serial_number = models.IntegerField()
    marks = models.IntegerField()

    class Meta:
        unique_together = ('exam', 'question')

    def __str__(self):
        return f"{self.exam.exam_name} - {self.question.question_text}"