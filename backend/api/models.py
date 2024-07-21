from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('coach', 'Coach'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    # Add related_name to avoid conflicts
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='api_users',  
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='api_users',  
        blank=True
    )

class Lesson(models.Model):
    coach = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'coach'})
    date = models.DateField()
    time = models.TimeField()
    duration = models.IntegerField()
    STATUS_CHOICES = (
        ('available', 'Available'),
        ('booked', 'Booked'),
        ('completed', 'Completed'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

class Booking(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'student'})
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    STATUS_CHOICES = (
        ('booked', 'Booked'),
        ('canceled', 'Canceled'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

class Review(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
