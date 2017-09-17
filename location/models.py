from __future__ import unicode_literals

from django.db import models
from action.models import ModernModel
import uuid


class PositionModel(ModernModel):
    """
    Each record presents a specific position
    """
    position_x = models.DecimalField(
        blank=False, null=False, max_digits=10, decimal_places=6,
        help_text="horizontal axis value in current location's coordinate system")
    position_y = models.DecimalField(
        blank=False, null=False, max_digits=10, decimal_places=6,
        help_text="vertical axis value in current location's coordinate system")
    position_orientation = models.DecimalField(
        blank=True, null=True, max_digits=10, decimal_places=6,
        help_text="entity's facing direction, for example facing north takes "
            "value '0', facing southwest takes value '225'.")
    position_accuracy = models.CharField(
        max_length=30, blank=False, null=False,
        help_text="confidence level of the position_[x|y|orientation] values"
    )
    class Meta:
		abstract = True


class Position(PositionModel):
    """
    Each record presents one user's point of time and space
    """
    # TODO: realize the below fields
    # user_guid, # FK ref.
    # location_guid, # FK to estimote_locations
    # TODO: update below precision level once get real value from estimote.
    location_id = models.CharField(
        max_length=20, blank=False, null=False,
        help_text="need to use FK once location model is built"
    )
