from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    date = models.DateField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_finished = models.BooleanField(default=False)
    id = models.CharField(max_length=6, primary_key=True)