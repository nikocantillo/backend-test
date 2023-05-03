import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from core_base.domain.base_model import BaseModel


class User(AbstractUser, BaseModel):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False
    )
    identification = models.CharField(
        max_length=100,
        blank=False, 
        null=True, 
        db_column='identification'
    )
    email = models.EmailField(
        blank=True, 
        unique=True, 
        db_column='email'
    )
    date_joined = models.DateTimeField(
        auto_now=True, 
        verbose_name = 'Fecha de actualización', 
        null=True,
        db_column='date_joined'
    )
    phone = models.JSONField(null=True)

    class Meta(AbstractUser.Meta):
        ordering = ['id']
        swappable = "AUTH_USER_MODEL"
        db_table = "user"

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [""]