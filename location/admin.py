from django.contrib import admin
from location.models import ExhibitPosition
from location.models import UserPositionHistory

@admin.register(ExhibitPosition)
class ExhibitPositionAdmin(admin.ModelAdmin):
    list_display = [
        'guid', 'position_x', 'position_y',
        'position_orientation', 'position_accuracy',
        'position_x_left', 'position_x_right',
        'position_y_lower', 'position_y_upper',
		'create_dt',
    ]
    search_fields = ['guid', 'position_x']
    list_filter = ['position_accuracy']


@admin.register(UserPositionHistory)
class UserPositionHistoryAdmin(admin.ModelAdmin):
    list_display = [
        'guid', 'position_x', 'position_y',
        'position_orientation', 'position_accuracy',
		'create_dt',
    ]
    search_fields = ['guid', 'position_x']
    list_filter = ['position_accuracy']

