from django.contrib.auth.models import User
from django.db import models


class Chore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="chores")
    name = models.CharField(max_length=255, null=False, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name="created_chores"
    )
    completed_on = models.DateTimeField()
    score = models.PositiveSmallIntegerField(default=1)
