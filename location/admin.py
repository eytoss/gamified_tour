from django.contrib import admin
from location.models import UserPosition

@admin.register(UserPosition)
class UserPositionAdmin(admin.ModelAdmin):
    list_display = [
        'guid', 'position_x', 'position_y',
        'position_orientation', 'position_accuracy',
		'create_dt',
    ]
    search_fields = ['guid', 'position_x']
    list_filter = ['position_accuracy']

