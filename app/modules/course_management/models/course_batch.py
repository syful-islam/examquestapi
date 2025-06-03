from django.db import models
from app.modules.general_module.models.base_model import BaseModel
from .course import Course

class CourseBatch(BaseModel):
    #batch_id = models.AutoField(primary_key=True)
    batch_id = models.CharField(max_length=50, unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    batch_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.batch_name