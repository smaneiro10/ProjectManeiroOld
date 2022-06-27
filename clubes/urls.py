from django.urls import path
from clubes import views

app_name='clubes'
urlpatterns = [
    path('', views.ClubesListView.as_view(), name='clubes-list'),
    path('add/', views.ClubesCreateView.as_view(), name='clubes-add'),
    path('<int:pk>/detail', views.ClubesDetailView.as_view(), name='clubes-detail'),
    path('<int:pk>/update', views.ClubesUpdateView.as_view(), name='clubes-update'),
    path('<int:pk>/delete', views.ClubesDeleteView.as_view(), name='clubes-delete'),

]