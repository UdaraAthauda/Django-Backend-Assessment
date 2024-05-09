from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('student', views.student, name='student'),
    path('school', views.school, name='school'),
    path('class', views.classes, name='class'),
    path('assessment', views.assessment, name='assessment'),
    path('answers', views.answers, name='answers'),
    path('awards', views.awards, name='awards'),
    path('subject', views.subject, name='subject'),

]
