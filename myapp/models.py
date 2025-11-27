# wordle/models.py (o la carpeta de tu aplicación)

from django.db import models

class Character(models.Model):
    Name = models.CharField(max_length=100)
    AgeRange = models.CharField(max_length=10)
    Occupation = models.CharField(max_length=100)
    Genre = models.CharField(max_length=10)
    PlaceOfLiving = models.CharField(max_length=100)
    FirstAppearance = models.CharField(max_length=10)

    class Meta:
        db_table = 'CHARACTER'  # Nombre real de la tabla en la BB

    def __str__(self):
        return self.Name