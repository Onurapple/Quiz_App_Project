from django.urls import path
from .views import QuizView, CategoryView, QuestionView, QuizListCreateView, QuestionListCreateView, AnswerView
#from rest_framework import routers



#router = routers.DefaultRouter()
#router.register(r'category', CategoryView)
#router.register(r'quiz', QuizView)
#router.register(r'question', QuestionView)




urlpatterns = [

    path('', CategoryView.as_view({'get': 'list'})), 
    path('answer/', AnswerView.as_view({'get': 'list'})), 
    path('<str:category>/', QuizView.as_view({'get': 'list'})),
    path('<str:category>/<str:quiz>', QuestionView.as_view({'get': 'list'}))
]

#urlpatterns += router.urls
# router = routers.DefaultRouter()
# router.register('', CategoryView)
# router.register('answers/', AnswerView)
# router.register('<str:category>/', QuizView)
# router.register('<str:category>/<str:quiz>', QuestionView)



#router.register('quizes', QuizView)
# router.register('categories', CategoryView)
# router.register('questions', QuestionView)





# urlpatterns = [
    
# ]


