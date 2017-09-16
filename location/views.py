from django.http import HttpResponse
from location.models import Position

def welcome(request):
    pos = Position.objects.create(
        position_x = 3,
        position_y = 4
    )
    return HttpResponse("There is no spoon. You know where you are.")
