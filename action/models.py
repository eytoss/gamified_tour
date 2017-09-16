from __future__ import unicode_literals

from django.db import models
import uuid

class ExhibitAction(models.Model):
    """
    Each record presents one available user-interactive action provided by the exhibit
    """
    guid = models.CharField(
        max_length=36, blank=True, unique=True, default=uuid.uuid4,
        help_text="Unique, externally-friendly identifier for action"
    )
    # TODO: realize the below fields
    # exhibit_guid, # FK ref.
    create_dt = models.DateTimeField(auto_now=True)
    details = models.CharField(
        max_length=20, blank=False, null=False,
        help_text="indicate action type, # TODO: will improve this field"
    )

