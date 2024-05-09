from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . models import *

# Create your views here.
def home(request):
    return render(request, 'home.html')

def student(request):
    details = Student.objects.all()
    dict = {
        'student': details
    }
    return render(request, 'student.html', context=dict)

def school(request):
    details = School.objects.all()
    dict = {
        'school': details
    }
    return render(request, 'school.html', context=dict)

def classes(request):
    details = Class.objects.all()
    dict = {
        'class': details
    }
    return render(request, 'class.html', context=dict)

def assessment(request):
    details = AssessmentAreas.objects.all()
    dict = {
        'assessment': details
    }
    return render(request, 'assessment.html', context=dict)

def answers(request):
    details = Answers.objects.all()
    dict = {
        'answers': details
    }
    return render(request, 'answers.html', context=dict)

def awards(request):
    details = Awards.objects.all()
    dict = {
        'awards': details
    }
    return render(request, 'awards.html',context=dict)

def subject(request):
    details = Subject.objects.all()
    dict = {
        'subject': details
    }
    return render(request, 'subject.html', context=dict)
