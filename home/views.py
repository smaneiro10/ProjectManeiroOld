from django.shortcuts import render
from django.db.models import Q

from jugadores.models import Jugadores
from user.models import Avatar


def index(request):
    inicio=False
    avatar_ctx = get_avatar_url_ctx(request)
    context_dict = {**avatar_ctx}
    jugadores = Jugadores.objects.all()
    context_dict.update({
        'jugadores': jugadores, 'inicio':inicio
    })
    return render(
        request=request,
        context=context_dict,
        template_name="main.html"
    )

def get_avatar_url_ctx(request):
    avatars = Avatar.objects.filter(user=request.user.id)
    if avatars.exists():
        return {"url": avatars[0].image.url}
    return {}


def search(request):
    inicio = True
    avatar_ctx = get_avatar_url_ctx(request)
    context_dict = {**avatar_ctx}
    if request.GET['search_param']:
        search_param = request.GET['search_param']
        query = Q(nombre__contains=search_param)
        query.add(Q(equipo__contains=search_param), Q.OR)
        jugadores = Jugadores.objects.filter(query)
        context_dict.update({
            'jugadores': jugadores,
            'search_param': search_param,
            'inicio':inicio
        })
    return render(
        request=request,
        context=context_dict,
        template_name="main.html",
    )

def contacto(request):
    context_dict = {
        'n1': 'Santiago Martín Maneiro'
    }
    
    return render(
        request=request,
        context=context_dict,
        template_name="contacto.html",
    )

def acerca_de(request):
    context_dict = {
        'n1': 'Santiago Martín Maneiro'
    }
    
    return render(
        request=request,
        context=context_dict,
        template_name="acerca_de.html",
    )
