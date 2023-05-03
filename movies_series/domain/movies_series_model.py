from django.db import models
from core_base.domain.base_model import BaseModel
from movies_series.domain.types_model import Type
from movies_series.domain.gender_model import Gender


class MovieSeries(BaseModel):

    name = models.CharField(
        max_length=255
    )
    genre = models.ManyToManyField(Gender)
    type = models.ForeignKey(
        Type, 
        on_delete=models.CASCADE
    )
    number_of_views = models.PositiveIntegerField(
        default=0
    )
    total_score = models.PositiveIntegerField(
        default=0
    )
    number_of_ratings = models.PositiveIntegerField(
        default=0
    )

    def average_score(self):
        if self.no_of_ratings == 0:
            return 0
        return self.total_score / self.no_of_ratings

    def __str__(self):
        return self.name