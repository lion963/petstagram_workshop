from django.db import models


class Pet(models.Model):
    TYPE_CHOICES = (
        ('cat', 'cat'),
        ('dog', 'dog'),
        ('parrot', 'parrot')
    )
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    name = models.CharField(max_length=6)
    age = models.PositiveIntegerField(null=True)
    description = models.TextField(null=True)
    image_url = models.URLField(null=True)


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, null=True)
