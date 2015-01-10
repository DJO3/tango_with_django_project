from django.http import HttpResponse


def index(request):
    return HttpResponse("Link to the About page: <br/> <a href='/rango/about'>About</a>")


def about(request):
    return HttpResponse("Link to the Home page: <br/> <a href='/rango/'>Home</a>")