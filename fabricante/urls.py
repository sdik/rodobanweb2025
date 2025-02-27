from django.urls import path
from . import views

app_name = 'fabricante'

urlpatterns = [
    path('', views.FabricanteListView.as_view(), name='fabricante_list'),
    path('novo/', views.FabricanteCreateView.as_view(), name='fabricante_create'),
    path('<int:pk>/editar/', views.FabricanteUpdateView.as_view(), name='fabricante_update'),
    path('<int:pk>/excluir/', views.FabricanteDeleteView.as_view(), name='fabricante_delete'),
    path('<int:pk>/detalhes/', views.FabricanteDetailView.as_view(), name='fabricante_detail'),
] 