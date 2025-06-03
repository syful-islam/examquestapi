from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.modules.access_control.views.eq_user import EQUserViewSet
from .modules.general_module.views.list_of_value import LovView, LovAllowAnyView
from .modules.auth.views.login import LoginView,RegisterView, ChangePasswordView, LogoutView, ForgotPasswordView, ResetPasswordView
from .modules.auth.views.otp import SendOTPView,ValidateOTPView,SendNotificationView
from app.modules.course_management.views.course import CourseViewSet
from app.modules.course_management.views.course_section import CourseSectionViewSet
from app.modules.course_management.views.course_batch import CourseBatchViewSet
from app.modules.exam_management.views.question import QuestionViewSet
from app.modules.exam_management.views.question_option import QuestionOptionViewSet
from app.modules.exam_management.views.answer_option import AnswerOptionViewSet
from app.modules.exam_management.views.exam import ExamViewSet
from app.modules.exam_management.views.exam_question import ExamQuestionViewSet
from app.modules.student_management.views.student import StudentViewSet
from app.modules.student_management.views.student_course import StudentCourseViewSet
from app.modules.student_management.views.student_exam import StudentExamViewSet
from app.modules.student_management.views.student_exam_question import StudentExamQuestionViewSet
from app.modules.student_management.views.student_exam_answer import StudentExamAnswerViewSet

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r'users', EQUserViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'course-sections', CourseSectionViewSet)
router.register(r'course-batches', CourseBatchViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'question-options', QuestionOptionViewSet)
router.register(r'answer-options', AnswerOptionViewSet)
router.register(r'exams', ExamViewSet)
router.register(r'exam-questions', ExamQuestionViewSet)
router.register(r'students', StudentViewSet)
router.register(r'student-courses', StudentCourseViewSet)
router.register(r'student-exams', StudentExamViewSet)
router.register(r'student-exam-questions', StudentExamQuestionViewSet)
router.register(r'student-exam-answers', StudentExamAnswerViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),  # Add the login view here
    path('register/', RegisterView.as_view(), name='login'),  # Add the login view here
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),  # Add the login view here
    path('reset-password/', ResetPasswordView.as_view(), name='change_password'),  # Add the login view here
    path('lov/<str:model>/', LovView.as_view(), name='lov'),
    path('lovallowany/<str:model>/', LovAllowAnyView.as_view(), name='lov'),
    path('send-otp/', SendOTPView.as_view(), name='send_otp'),
    path('validate-otp/', ValidateOTPView.as_view(), name='validate_otp'),
    path('send-notification/', SendNotificationView.as_view(), name='send_notification'),
]


# urlpatterns = [
#     path('users/', get_users, name='get_users'),
#     path('users/create/', create_user, name='create_user'),
#     path('users/<int:pk>/', user_detail, name='user_detail'),
#     path('courses/', get_courses, name='get_courses'),
#     path('courses/create/', create_course, name='create_course'),
#     path('courses/<int:pk>/', course_detail, name='course_detail'),
#     path('course_sections/', get_course_sections, name='get_course_sections'),
#     path('course_sections/create/', create_course_section, name='create_course_section'),
#     path('course_sections/<int:pk>/', course_section_detail, name='course_section_detail'),
#     path('course_batches/', get_course_batches, name='get_course_batches'),
#     path('course_batches/create/', create_course_batch, name='create_course_batch'),
#     path('course_batches/<int:pk>/', course_batch_detail, name='course_batch_detail'),
#     path('questions/', get_questions, name='get_questions'),
#     path('questions/create/', create_question, name='create_question'),
#     path('questions/<int:pk>/', question_detail, name='question_detail'),
#     path('question_options/', get_question_options, name='get_question_options'),
#     path('question_options/create/', create_question_option, name='create_question_option'),
#     path('question_options/<int:pk>/', question_option_detail, name='question_option_detail'),
#     path('answer_options/', get_answer_options, name='get_answer_options'),
#     path('answer_options/create/', create_answer_option, name='create_answer_option'),
#     path('answer_options/<int:pk>/', answer_option_detail, name='answer_option_detail'),
#     path('exams/', get_exams, name='get_exams'),
#     path('exams/create/', create_exam, name='create_exam'),
#     path('exams/<int:pk>/', exam_detail, name='exam_detail'),
#     path('exam_questions/', get_exam_questions, name='get_exam_questions'),
#     path('exam_questions/create/', create_exam_question, name='create_exam_question'),
#     path('exam_questions/<int:pk>/', exam_question_detail, name='exam_question_detail'),
#     path('students/', get_students, name='get_students'),
#     path('students/create/', create_student, name='create_student'),
#     path('students/<int:pk>/', student_detail, name='student_detail'),
#     path('student_courses/', get_student_courses, name='get_student_courses'),
#     path('student_courses/create/', create_student_course, name='create_student_course'),
#     path('student_courses/<int:pk>/', student_course_detail, name='student_course_detail'),
#     path('student_exams/', get_student_exams, name='get_student_exams'),
#     #path('student_exams/create/', create_student_exam, name='create_student_exam'),
#     path('student_exams/<int:pk>/', student_exam_detail, name='student_exam_detail'),
#     path('student_exams/appear/', create_student_exam, name='create_student_exam'),
#     path('student_exams/appear/<int:pk>/', student_exam_detail, name='student_exam_detail'),
#     #path('student_exams/submit/', create_student_exam, name='submit_student_exam'),
#     path('student_exam_questions/<int:exam_id>/', get_student_exam_questions, name='get_student_exam_questions'),
#     path('student_exam_answers/', get_student_exam_answers, name='get_student_exam_answers'),
#     path('student_exam_answers/create/', create_student_exam_answer, name='create_student_exam_answer'),
#     path('student_exam_answers/<int:pk>/', student_exam_answer_detail, name='student_exam_answer_detail'),
# ]