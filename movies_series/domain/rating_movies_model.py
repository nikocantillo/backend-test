from django.db import models
from authentication.domain.user import User
from core_base.domain.base_model import BaseModel
from movies_series.domain.types_model import Type


class Movie(BaseModel):
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='movies_series')
    viewed_by = models.ManyToManyField(User, related_name='movies_watched', blank=True)
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Película o Serie"
        verbose_name_plural = "Películas y Series"
        ordering = ['name']

class UsersRating(BaseModel):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    rating = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        return f"{self.user} - {self.movie} - {self.rating}"

    class Meta:
        verbose_name = "Puntuación de Usuario"
        verbose_name_plural = "Puntuaciones de Usuarios"
        unique_together = ['movie', 'user']