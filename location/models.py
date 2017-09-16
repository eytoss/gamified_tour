from __future__ import unicode_literals

from django.db import models

class Position(models.Model):
    """
    Each record presents one user's point of time and space
    """
    guid = models.CharField(
        max_length=36, blank=True, unique=True, default=uuid.uuid4,
        help_text="Unique, externally-friendly identifier for position"
    )
    # TODO: realize the below fields
    # user_guid, # FK ref.
    # location_guid, # FK to estimote_locations
    create_dt = models.DateTimeField(auto_now=True)
    # TODO: update below precision level once get real value from estimote.
    position_x = models.DecimalField(
        blank=False, null=False, max_digits=6, decimal_places=4,
        help_text="horizontal axis value in current location’s coordinate system")
    position_y = models.DecimalField(
        blank=False, null=False, max_digits=6, decimal_places=4,
        help_text="vertical axis value in current location’s coordinate system")
    position_orientation = models.DecimalField(
        blank=True, null=True, max_digits=6, decimal_places=4,
        help_text="user’s facing direction, for example facing north takes "
            "value “0”, facing southwest takes value “225”.")
    position_accuracy = models.CharField(
        max_length=20, blank=False, null=False,
        help_text="confidence level of the position_[x|y|orientation] values"
    )
