from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    role = models.CharField(max_length=10, choices=[('student', 'Student'), ('coach', 'Coach'), ('admin', 'Admin')])

class Coach(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    availability = models.JSONField()

class Lesson(models.Model):
    student = models.ForeignKey(User, related_name='student_lessons', on_delete=models.CASCADE)
    coach = models.ForeignKey(User, related_name='coach_lessons', on_delete=models.CASCADE)
    time_slot = models.DateTimeField()
    status = models.CharField(max_length=10, choices=[('booked', 'Booked'), ('completed', 'Completed'), ('cancelled', 'Cancelled')])

class Review(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    coach = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

