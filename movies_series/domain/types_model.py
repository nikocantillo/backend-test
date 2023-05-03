from django.db import models
from core_base.domain.base_model import BaseModel

class Type(BaseModel):
    name = models.CharField(
        max_length=50, 
        unique=True
    )
    code = models.CharField(
        max_length=50, 
        unique=True
    )

    def __str__(self):
        return self.name