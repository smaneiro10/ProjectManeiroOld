from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from jugadores.models import Jugadores
from user.models import Avatar

class JugadoresListView(ListView):
    model = Jugadores
    template_name = "jugadores_list.html"

class JugadoresDetailView(DetailView):
    model = Jugadores
    template_name = "jugadores_detail.html"
    fields = ['nombre', 'equipo', 'fecha_nacimiento', 'descripcion']


class JugadoresCreateView(LoginRequiredMixin, CreateView):
    model = Jugadores
    template_name = "jugadores_add.html"
    success_url = reverse_lazy('jugadores:jugadores-list')
    fields = ['nombre', 'equipo', 'fecha_nacimiento', 'descripcion']


class JugadoresUpdateView(LoginRequiredMixin, UpdateView):
    model = Jugadores
    template_name = "jugadores_form.html"
    success_url = reverse_lazy('jugadores:jugadores-list')
    fields = ['nombre', 'equipo', 'fecha_nacimiento', 'descripcion']


class JugadoresDeleteView(LoginRequiredMixin, DeleteView):
    model = Jugadores
    template_name = "jugadores_confirm_delete.html"
    success_url = reverse_lazy('jugadores:jugadores-list')
