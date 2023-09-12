from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Chore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="chores")
