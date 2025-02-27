from django.urls import path
from . import views

app_name = 'produto'

urlpatterns = [
    path('', views.ProdutoListView.as_view(), name='produto_list'),
    path('novo/', views.ProdutoCreateView.as_view(), name='produto_create'),
    path('<int:pk>/editar/', views.ProdutoUpdateView.as_view(), name='produto_update'),
    path('<int:pk>/excluir/', views.ProdutoDeleteView.as_view(), name='produto_delete'),
    path('<int:pk>/detalhes/', views.ProdutoDetailView.as_view(), name='produto_detail'),
] 