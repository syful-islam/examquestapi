from django.db import models

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=100)
    # Add other basic info fields as needed

    def __str__(self):
        return self.student_name