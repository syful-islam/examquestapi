from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from app.modules.student_management.models import ExamQuestion, Question, QuestionOption, AnswerOption

@api_view(['GET'])
def get_student_exam_questions(request, exam_id):
    try:
        exam_questions = ExamQuestion.objects.filter(exam_id=exam_id).select_related('question')
    except ExamQuestion.DoesNotExist:
        return Response({'error': 'Exam not found'}, status=status.HTTP_404_NOT_FOUND)

    #print to console
    print(exam_questions.count())

    questions_data = []
    for exam_question in exam_questions:
        question = exam_question.question
        question_options = QuestionOption.objects.filter(question=question)
        answer_options = AnswerOption.objects.filter(question=question)

        options_data = []
        if question_options:
            options_data = [[option.option_text for option in question_options]]
            options_data.extend([[answer.answer_option_text for answer in answer_options]])
        else:
            options_data = [answer.answer_option_text for answer in answer_options]

        formatted_data = {
            'id': question.question_id,
            'questionSerialNo': exam_question.serial_number,
            'title': question.question_text,
            'type': question.question_type,
            'options': options_data,
            'answers': question.question_answer,
        }
        questions_data.append(formatted_data)

    return Response(questions_data, status=status.HTTP_200_OK)