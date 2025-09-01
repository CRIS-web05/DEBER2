from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



def home(request):
    return render(request, "home.html")

def colegio (request):
    if request.method =="GET":
        return render(request,
                      "colegio.html",
                      {"form":UserCreationForm})

    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(request.POST["username"],
                                                password=request.POST["password1"])
                user.save()
                return HttpResponse("Usuario creado correctamente")
            except Exception as e:
                return HttpResponse(f"Error al crear el usuario: {e}")
        else:
            return HttpResponse("Las contraseñas no coinciden")