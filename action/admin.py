from django.contrib import admin
from action.models import ExhibitAction

@admin.register(ExhibitAction)
class ExhibitActionAdmin(admin.ModelAdmin):
    list_display = [
        'guid', 'details',
        'create_dt',
    ]
    search_fields = ['guid', 'exhibit_guid']

