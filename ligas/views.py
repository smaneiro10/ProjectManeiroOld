from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from ligas.models import Ligas

class LigasListView(ListView):
    model = Ligas
    template_name = "ligas_list.html"


class LigasDetailView(DetailView):
    model = Ligas
    template_name = "ligas_detail.html"
    fields = ['torneo', 'equipos', 'internacional', 'descripcion']


class LigasCreateView(LoginRequiredMixin, CreateView):
    model = Ligas
    template_name = "ligas_add.html"
    success_url = reverse_lazy('ligas:ligas-list')
    fields = ['torneo', 'equipos', 'internacional', 'descripcion']


class LigasUpdateView(LoginRequiredMixin, UpdateView):
    model = Ligas
    template_name = "ligas_form.html"
    success_url = reverse_lazy('ligas:ligas-list')
    fields = ['torneo', 'equipos', 'internacional', 'descripcion']


class LigasDeleteView(LoginRequiredMixin, DeleteView):
    model = Ligas
    template_name = "ligas_confirm_delete.html"
    success_url = reverse_lazy('ligas:ligas-list')

# def es_internacional(request):
#     if Ligas.internacional is True:
#         return f'Si'
#     else:
#         return f'No'
