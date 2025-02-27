from django.urls import path
from . import views

app_name = 'cliente'

urlpatterns = [
    path('', views.ClienteListView.as_view(), name='cliente_list'),
    path('novo/', views.ClienteCreateView.as_view(), name='cliente_create'),
    path('<int:pk>/editar/', views.ClienteUpdateView.as_view(), name='cliente_update'),
    path('<int:pk>/excluir/', views.ClienteDeleteView.as_view(), name='cliente_delete'),
    path('<int:pk>/detalhes/', views.ClienteDetailView.as_view(), name='cliente_detail'),
] 