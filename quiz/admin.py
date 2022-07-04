from django.contrib import admin
from .models import Answer, Category, Question, Quiz
import nested_admin


class AnswerInline(nested_admin.NestedTabularInline):
    model = Answer
    min_num = 2
    max_num = 5
    extra = 1

class QuestionInline(nested_admin.NestedStackedInline):
    model = Question
    extra = 1
    inlines = [AnswerInline]

class QuizAdmin(nested_admin.NestedModelAdmin):
    model = Quiz
    inlines = [QuestionInline]
    list_display = ('title', 'category', 'question_count')
    list_filter = ('category',)
    search_fields = ('title',)
    ordering = ('title',)


admin.site.register(Quiz, QuizAdmin)
admin.site.register([ Category,])

# admin.site.register(Quiz)
# admin.site.register(Category)
# admin.site.register(Question)
# admin.site.register(Answer)


admin.site.site_title = " Quiz App Project"
admin.site.site_header = "Quiz App Admin Portal"
admin.site.index_title = "Welcome to Quiz App Admin Portal"