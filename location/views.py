from django.http import HttpResponse

def welcome(request):
    return HttpResponse("In Location: There is no spoon. You know where you are.")

