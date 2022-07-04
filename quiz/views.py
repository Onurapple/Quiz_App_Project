from .serializers import QuizSerializer, CategorySerializer, QuestionSerializer, AnswerSerializer
from .models import Answer, Question, Quiz, Category
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from  rest_framework.generics import ListCreateAPIView

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

class QuizView(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class QuestionView(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuizListCreateView(ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        if category:
            return Quiz.objects.filter(category=category)
        return Quiz.objects.all()

class QuestionListCreateView(ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    #permission_classes = (IsAdminUser ,)

    def get_queryset(self):
        quiz = self.kwargs['quiz']
        if quiz:
            return Question.objects.filter(quiz=quiz)
        return Question.objects.all()

class AnswerView(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


