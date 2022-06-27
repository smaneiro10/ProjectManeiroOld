from django.urls import path
from ligas import views

app_name='ligas'
urlpatterns = [
    path('', views.LigasListView.as_view(), name='ligas-list'),
    path('add/', views.LigasCreateView.as_view(), name='ligas-add'),
    path('<int:pk>/detail', views.LigasDetailView.as_view(), name='ligas-detail'),
    path('<int:pk>/update', views.LigasUpdateView.as_view(), name='ligas-update'),
    path('<int:pk>/delete', views.LigasDeleteView.as_view(), name='ligas-delete'),
]