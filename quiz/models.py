from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=20, primary_key=True, unique=True)
    
    def __str__(self):
        return f'{self.name}'

    def quiz_count(self):
        return self.quizzes.count()


class Quiz(models.Model):
    title = models.CharField(max_length=200, primary_key=True)
    date_created = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='quizzes')
    
    def __str__(self):
        return f'{self.title}'

    def question_count(self):
        return self.question.count()




class Question(models.Model):
    difficult = [('H', 'Hard'), ('M', 'Medium'), ('E', 'Easy')]
    title = models.CharField(max_length=200, primary_key=True)
    difficulty = models.CharField(max_length=1, choices=difficult, default='M')
    date_created = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='question')
    def __str__(self):
        return f'{self.title} - {self.difficulty}'


class Answer(models.Model):
    answer_text = models.TextField(primary_key=True)
    is_right = models.BooleanField()
    updated_date = models.DateField(auto_now=True)
    questions = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer')
    def __str__(self):
        return f'{self.answer_text} - {self.is_right} - {self.updated_date} - {self.questions}'



