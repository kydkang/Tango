from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
#   return HttpResponse("This is about page  <br/> <a href='/rango/'>Index</a>")
    context_dict = {'about_string': "This is about page.", 'my_name': "KYD" }
    return render(request, 'rango/about.html', context=context_dict)