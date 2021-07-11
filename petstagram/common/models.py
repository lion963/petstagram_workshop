from django.db import models

from accounts.models import UserProfile
from pets.models import Pet


class Comment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, null=True)
    comment = models.TextField(null=True)