from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from movies.models import Movie


class Review(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.PROTECT,
        related_name='reviews'
    )
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, 'Avaliação não deve ser menor que 0'),
            MaxValueValidator(5, 'Avaliação não deve ser maior que 5'),
        ]
    )
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.movie)