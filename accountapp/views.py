from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def hello_world(request):
    if request.method == "post":
        return render(request, 'accountapp/hellow_world.html',
                  context={'text': 'POST METHOD'})

    else:
        return render(request, 'accountapp/hellow_world.html',
                  context={'text': 'POST METHOD'})
