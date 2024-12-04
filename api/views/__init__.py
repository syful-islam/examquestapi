from .user import get_users, create_user, user_detail
from .course import get_courses, create_course, course_detail
from .course_section import get_course_sections, create_course_section, course_section_detail
from .course_batch import get_course_batches, create_course_batch, course_batch_detail
from .question import get_questions, create_question, question_detail
from .question_option import get_question_options, create_question_option, question_option_detail
from .answer_option import get_answer_options, create_answer_option, answer_option_detail
from .exam import get_exams, create_exam, exam_detail
from .exam_question import get_exam_questions, create_exam_question, exam_question_detail
from .student import get_students, create_student, student_detail
from .student_course import get_student_courses, create_student_course, student_course_detail
from .student_exam import get_student_exams, create_student_exam, student_exam_detail
from .student_exam_question import get_student_exam_questions
from .student_exam_answer import get_student_exam_answers, create_student_exam_answer, student_exam_answer_detail