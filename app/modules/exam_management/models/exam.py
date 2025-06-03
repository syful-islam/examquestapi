from django.db import models
from app.modules.general_module.models.base_model import BaseModel
from app.modules.course_management.models.course import Course
from app.modules.course_management.models.course_batch import CourseBatch
from app.modules.course_management.models.course_section import CourseSection

class Exam(BaseModel):
    # exam_id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    batch = models.ForeignKey(CourseBatch, on_delete=models.CASCADE)
    exam_name = models.CharField(max_length=100)
    enrollment_based = models.BooleanField(default=False)
    exam_date = models.DateField()
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()
    include_sections = models.ManyToManyField(CourseSection, related_name='included_exams', blank=True)
    exclude_sections = models.ManyToManyField(CourseSection, related_name='excluded_exams', blank=True)
    exclude_previous_exams = models.BooleanField(default=False)
    question_per_section = models.IntegerField()
    display_question_answer = models.BooleanField(default=False)
    display_exam_result = models.BooleanField(default=False)
    total_num_of_questions = models.IntegerField()
    randomize_question = models.BooleanField(default=False)
    default_marks_per_question = models.IntegerField(default=1)
    pass_mark = models.IntegerField()

    def __str__(self):
        return self.exam_name