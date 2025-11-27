#from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db.models.functions import Upper
from django.db.models import Q
from datetime import date
import random
import json

from .models import Character

def iniPage(request):
    return HttpResponse("Hello world")

def home(request):
    return render(request, 'home.html')

def index(request):
    title = 'Prueba1'
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':  # Verifica si el método es POST
        username = request.POST.get('username')  # Obtiene el valor del campo 'username'
        password = request.POST.get('password')  # Obtiene el valor del campo 'password'

        # Aquí puedes añadir la lógica para autenticar al usuario
        if username == "admin" and password == "1234":  # Ejemplo de autenticación básica
            return HttpResponse(f"¡Bienvenido, {username}!")
        else:
            return HttpResponse("Credenciales inválidas. Inténtalo de nuevo.")
    return render(request, 'login.html')  # Renderiza el formulario si no es POST

def getNames(request):
    term = request.GET.get("term", "")
    #names = list(CHARACTER.objects.filter(name__icontains = term).values_list("name", flat = True)[:10])
    names = list(
        Character.objects.filter(
            Q(Name__istartswith=term) |
            Q(Name__icontains=" " + term)  # apellido empieza con term
        ).values_list("Name", flat=True)[:10]
    )
    
    print(JsonResponse(names, safe = False))
    print(names)
    return JsonResponse(names, safe = False)

def getinfo(request):
    name = request.GET.get("name", "")
    try:
        character = Character.objects.get(Name=name)
        data = {
            "Name": character.Name,
            "AgeRange": character.AgeRange,
            "Occupation": character.Occupation,
            "Genre": character.Genre,
            "PlaceOfLiving": character.PlaceOfLiving,
            "FirstAppearance": character.FirstAppearance,
        }
        return JsonResponse(data)
    except Character.DoesNotExist:
        return JsonResponse({"error": "Character not found"}, status=404)

def getCorrectCharacter(request):

    all_chars = list(Character.objects.all())
    if not all_chars:
        return JsonResponse({"error": "No characters in database"}, status=500)

    today = date.today()

    # Convertir la fecha en número (ej. 20250214)
    seed_value = int(today.strftime("%Y%m%d"))

    random.seed(seed_value)
    correct = random.choice(all_chars)

    data = {
        "Name": correct.Name,
        "AgeRange": correct.AgeRange,
        "Occupation": correct.Occupation,
        "Genre": correct.Genre,
        "PlaceOfLiving": correct.PlaceOfLiving,
        "FirstAppearance": correct.FirstAppearance,
    }

    return JsonResponse(data)