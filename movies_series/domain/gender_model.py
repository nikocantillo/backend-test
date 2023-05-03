from core_base.domain.base_model import BaseModel
from django.db import models


class Gender(BaseModel):
    name = models.CharField(
        max_length=100, 
        null=True, 
        blank=True
    )
    code = models.CharField(
        max_length=100, 
        null=True, 
        blank=True,
        unique=True
    )

    def __str__(self):
        return self.name