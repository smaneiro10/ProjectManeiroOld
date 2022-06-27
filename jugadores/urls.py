from django.urls import path
from jugadores import views

app_name='jugadores'
urlpatterns = [
    path('', views.JugadoresListView.as_view(), name='jugadores-list'),
    path('add/', views.JugadoresCreateView.as_view(), name='jugadores-add'),
    path('<int:pk>/detail', views.JugadoresDetailView.as_view(), name='jugadores-detail'),
    path('<int:pk>/update', views.JugadoresUpdateView.as_view(), name='jugadores-update'),
    path('<int:pk>/delete', views.JugadoresDeleteView.as_view(), name='jugadores-delete'),
]
