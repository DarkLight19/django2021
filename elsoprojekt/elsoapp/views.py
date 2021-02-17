from django.shortcuts import render

# Create your views here.
from .models import Tanulo, Valasztas, Foglalkozas

def home_view(request, *args, **kwargs):

    tanulok = Tanulo.objects.all()

    kontextus = {
    "a": 123,
    "b": "blablabla",
    "l": [1,3,5,7,9],
    "tanulok": tanulok,
    }
    print(f"Akontextus a. eleme: {kontextus['a']}")
    return render(request, "home.html", kontextus)

def tesijel(request):
    foglalkozasnevek = Foglalkozas.objects.all()
    kontextus = {"foglalkozasok": Foglalkozas.objects.all()}
    return render(request, "tesi.html", kontextus)
