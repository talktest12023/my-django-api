from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Hello, Django! Your project is working.</h1>")
