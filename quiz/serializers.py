from rest_framework import serializers
from .models import Category, Quiz, Question, Answer



class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = (
            'answer_text',
            'is_right',
            'updated_date',
            'questions'
        )


class QuestionSerializer(serializers.ModelSerializer):
    answers=AnswerSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields =(
            'title',
            'difficulty',
            #'date_created',
            #'updated_date',
            #'quiz',
            'answers',
            'answer'
        )

class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    class Meta:
        model = Quiz
        fields = (
            'title',
            'question_count',
            'category',
            #'date_created',
            'question',
            'questions'
        )

    def create(self, validated_data):
        questions = validated_data.pop('question')

        quiz = Quiz.objects.create(**validated_data)
        for question in questions:
            answers = question.pop('answers')
            questionNew=Question.objects.create(quiz=quiz, **question)
            for answer in answers:
                Answer.objects.create(question=questionNew, **answer)
        return quiz


class CategorySerializer(serializers.ModelSerializer):
    quiz = QuizSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = (
            'name',
            'quiz_count',
            'quiz'
            #'quizzes'
            
        )



