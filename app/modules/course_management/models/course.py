from django.db import models
from app.modules.general_module.models.base_model import BaseModel

class Course(BaseModel):
    course_id = models.CharField(max_length=50, unique=True)
    course_name = models.CharField(max_length=100, unique=True)
    chapter_alias = models.CharField(max_length=50, default='Chapter')
    section_alias = models.CharField(max_length=50, default='Section')
    subsection_alias = models.CharField(max_length=50, default='Subsection')

    def __str__(self):
        return self.course_name