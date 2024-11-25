from django.db import models
from .course_section import CourseSection

class Question(models.Model):
    MEDIA_TYPE_CHOICES = [
        ('image', 'Image'),
        ('audio', 'Audio'),
        ('video', 'Video'),
    ]

    QUESTION_TYPE_CHOICES = [
        ('radio', 'Radio'),
        ('check', 'Check'),
        ('order', 'Order'),
        ('pair', 'Pair'),
    ]

    DIFFICULTY_LEVEL_CHOICES = [
        (3, 'High'),
        (2, 'Medium'),
        (1, 'Low'),
    ]

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    question_id = models.AutoField(primary_key=True)
    section = models.ForeignKey(CourseSection, on_delete=models.CASCADE)
    question_text = models.TextField()
    media_url = models.URLField(blank=True, null=True)
    media_type = models.CharField(max_length=5, choices=MEDIA_TYPE_CHOICES, blank=True, null=True)
    question_type = models.CharField(max_length=5, choices=QUESTION_TYPE_CHOICES)
    question_answer = models.JSONField()
    difficulty_level = models.IntegerField(choices=DIFFICULTY_LEVEL_CHOICES)
    note = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)

    def __str__(self):
        return self.question_text