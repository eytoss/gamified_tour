from django.contrib import admin
from action.models import Action, ExhibitAction

@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    list_display = [
        'guid', 'code', "name", "action_type",
        "meta_data",
        'create_dt', "modify_dt"
    ]
    search_fields = ['name', 'code']


@admin.register(ExhibitAction)
class ExhibitActionAdmin(admin.ModelAdmin):
    list_display = [
        'details'
    ]

