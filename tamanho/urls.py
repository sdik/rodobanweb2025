from django.urls import path
from . import views

app_name = 'tamanho'

urlpatterns = [
    path('', views.TamanhoListView.as_view(), name='tamanho_list'),
    path('novo/', views.TamanhoCreateView.as_view(), name='tamanho_create'),
    path('<int:pk>/editar/', views.TamanhoUpdateView.as_view(), name='tamanho_update'),
    path('<int:pk>/excluir/', views.TamanhoDeleteView.as_view(), name='tamanho_delete'),
    path('<int:pk>/detalhes/', views.TamanhoDetailView.as_view(), name='tamanho_detail'),
] 