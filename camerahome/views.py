from django.shortcuts import render
from django.core.urlresolvers import reverse

# Create your views here.


def home(request):
    context = {
        'url': reverse('home')
    }
    return render(request, "camerahome/home.html", context)
