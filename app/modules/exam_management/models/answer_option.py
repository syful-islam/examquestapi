from django.db import models
from app.modules.general_module.models.base_model import BaseModel
from .question import Question
from .question_option import QuestionOption

class AnswerOption(BaseModel):
    MEDIA_TYPE_CHOICES = [
        ('image', 'Image'),
        ('audio', 'Audio'),
        ('video', 'Video'),
    ]

    # answer_option_id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    question_option = models.ForeignKey(QuestionOption, on_delete=models.CASCADE, blank=True, null=True)
    answer_option_text = models.TextField()
    media_url = models.URLField(blank=True, null=True)
    media_type = models.CharField(max_length=5, choices=MEDIA_TYPE_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.answer_option_text