from django.db import models
from core_base.domain.base_model import BaseModel
from authentication.domain import User
from movies_series.domain import MovieSeries


class UserRating(BaseModel):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    movie_series = models.ForeignKey(
        MovieSeries, 
        on_delete=models.CASCADE
    )
    rating = models.PositiveIntegerField(
        default=0
    )
    watched = models.BooleanField(
        default=False
    )

    class Meta:
        unique_together = ('user', 'movie_series')

    def __str__(self):
        return f"{self.user.username} - {self.movie_series.name}"