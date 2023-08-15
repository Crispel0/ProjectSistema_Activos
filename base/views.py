from django.contrib.auth import logout
from django.shortcuts import redirect, render

def salir(request):
    logout(request)
    return redirect('login')
