from django.http import HttpResponse

def welcome(request):
    return HttpResponse("There is no spoon. You know where you are.")
