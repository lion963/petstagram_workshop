from django.db import models

from pets.models import Pet


class Comment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, null=True)
    comment = models.TextField(null=True)
