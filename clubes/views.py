from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from clubes.models import Clubes


class ClubesListView(ListView):
    model = Clubes
    template_name = "clubes_list.html"


class ClubesDetailView(DetailView):
    model = Clubes
    template_name = "clubes_detail.html"
    fields = ['nombre', 'provincia', 'descripcion']


class ClubesCreateView(LoginRequiredMixin, CreateView):
    model = Clubes
    template_name = "clubes_add.html"
    success_url = reverse_lazy('clubes:clubes-list')
    fields = ['nombre', 'provincia', 'descripcion']


class ClubesUpdateView(LoginRequiredMixin, UpdateView):
    model = Clubes
    template_name = "clubes_form.html"
    success_url = reverse_lazy('clubes:clubes-list')
    fields = ['nombre', 'provincia', 'descripcion']


class ClubesDeleteView(LoginRequiredMixin, DeleteView):
    model = Clubes
    template_name = "clubes_confirm_delete.html"
    success_url = reverse_lazy('clubes:clubes-list')