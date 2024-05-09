from django.db import models

# Create your models here.
class Alldata(models.Model):
    school_name = models.CharField(max_length=50)
    year = models.DateField(max_length=5)
    StudentID = models.IntegerField()
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    YearLevel = models.IntegerField()
    Class = models.CharField(max_length=50)
    Subject = models.CharField(max_length=50)
    Answers = models.CharField(max_length=5)
    CorrectAnswers = models.CharField(max_length=5)
    QuestionNumber = models.IntegerField()
    SubjectContents = models.CharField(max_length=50)
    AssessmentAreas = models.CharField(max_length=50)
    sydney_correct_count_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    sydney_average_score = models.DecimalField(max_digits=5, decimal_places=2)
    sydney_participants = models.DecimalField(max_digits=5, decimal_places=2)
    student_score = models.DecimalField(max_digits=5, decimal_places=2)
    student_total_assessed = models.DecimalField(max_digits=5, decimal_places=2)
    student_area_assessed_score = models.DecimalField(max_digits=5, decimal_places=2)
    total_area_assessed_score = models.DecimalField(max_digits=5, decimal_places=2)
    participant = models.IntegerField()
    correct_answer_percentage_per_class = models.DecimalField(max_digits=5, decimal_places=2)
    average_score = models.DecimalField(max_digits=5, decimal_places=2)
    school_percentile = models.IntegerField()
    sydney_percentile = models.IntegerField()
    strength_status = models.CharField(max_length=5)
    high_distinct_count = models.IntegerField()
    distinct_count = models.IntegerField()
    credit_count = models.IntegerField()
    participant_count = models.IntegerField()
    award = models.CharField(max_length=50)

class Student(models.Model):
    fullname = models.CharField(max_length=50)

class School(models.Model):
    schoolName = models.CharField(max_length=50)

class Class(models.Model):
    Class = models.CharField(max_length=20)

class AssessmentAreas(models.Model):
    assessment = models.CharField(max_length=50)

class Answers(models.Model):
    answers = models.CharField(max_length=5)

class Awards(models.Model):
    awardName = models.CharField(max_length=50)

class Subject(models.Model):
    subject = models.CharField(max_length=50)
    score = models.DecimalField(max_digits=10, decimal_places=2)

