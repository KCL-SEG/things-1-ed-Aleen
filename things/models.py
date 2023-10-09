from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=False)
    description = models.CharField(blank=True, max_length=120)  # Limiting to 120 characters
    quantity = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    def __str__(self):
        return self.name
