from __future__ import unicode_literals

from django.db import models
import uuid


class ModernModel(models.Model):
    """
    served as base model
    """
    guid = models.CharField(
        max_length=36, blank=True, unique=True, default=uuid.uuid4,
        help_text="Unique, externally-friendly identifier"
    )
    create_dt = models.DateTimeField(auto_now_add=True)
    modify_dt = models.DateTimeField(auto_now=True, blank=True, null=True)
    meta_data = models.CharField(
        max_length=200, blank=True, null=True,
        help_text="All other available info of this record. "
            "Served as 1. Notes. OR 2. Extra info to support "
            "backfill should new fields are needed from here."
    )
    class Meta:
        abstract = True

class Action(ModernModel):
    """
    Each record represents one action that might be provided/taken by
        other entities.
    """
    code = models.CharField(max_length=50, blank=False, unique=True)
    name = models.CharField(max_length=50, blank=True, null=False)
    action_type = models.CharField(max_length=50, blank=True, unique=True)


class ExhibitAction(ModernModel):
    """
    Each record presents one available user-interactive action provided by the exhibit
    """
    # TODO: realize the below fields
    # exhibit_guid, # FK ref.
    details = models.CharField(
        max_length=200, blank=False, null=False,
        help_text="indicate action type, # TODO: will improve this field"
    )

