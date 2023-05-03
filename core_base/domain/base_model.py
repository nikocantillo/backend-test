import uuid
from django.db import models
from safedelete.models import SafeDeleteModel, SOFT_DELETE_CASCADE
from safedelete.models import SOFT_DELETE
from core_base.domain.manager import BasicManager


class BaseModel(SafeDeleteModel):
  id = models.UUIDField(
    primary_key=True, 
    default=uuid.uuid4, 
    editable=False
  )
  _safedelete_policy = SOFT_DELETE_CASCADE
  created_in = models.DateTimeField(
    auto_now_add=True,
    blank=True, 
    null=True, 
    verbose_name = 'Fecha de creación', 
    db_column='created_in'
  )
  modified_in = models.DateTimeField(
    auto_now=True, 
    verbose_name = 'Fecha de actualización', 
    null=True, 
    db_column='modified_in'
  )
  created_by = models.UUIDField(
    null=True, 
    editable=False, 
    db_column='created_by'
  )
  modified_by = models.UUIDField(
    null=True, 
    editable=False, 
    db_column='modified_by'
  )
  deleted_by = models.UUIDField(
    null=True, 
    editable=False, 
    db_column='deleted_by'
  )
  
  objects = BasicManager()

  class Meta:
    abstract = True