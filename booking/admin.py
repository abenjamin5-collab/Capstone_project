from django.contrib import admin
from .models import User, Coach, Lesson, Review

admin.site.register(User)
admin.site.register(Coach)
admin.site.register(Lesson)
admin.site.register(Review)

