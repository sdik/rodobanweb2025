from django.urls import path
from . import views

app_name = 'vendedor'

urlpatterns = [
    path('', views.VendedorListView.as_view(), name='vendedor_list'),
    path('novo/', views.VendedorCreateView.as_view(), name='vendedor_create'),
    path('<int:pk>/editar/', views.VendedorUpdateView.as_view(), name='vendedor_update'),
    path('<int:pk>/excluir/', views.VendedorDeleteView.as_view(), name='vendedor_delete'),
    path('<int:pk>/detalhes/', views.VendedorDetailView.as_view(), name='vendedor_detail'),
] 