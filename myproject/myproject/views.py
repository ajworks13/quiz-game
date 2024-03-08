from django.http import HttpResponse


def homepage(request):
    return HttpResponse("Hello world! Im home.")


def about(request):
    return HttpResponse("My about page.")
