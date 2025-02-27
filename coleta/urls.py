from django.urls import path
from . import views

app_name = 'coleta'

urlpatterns = [
    path('', views.coleta_list, name='coleta_list'),
    path('nova/', views.coleta_new, name='coleta_new'),
    path('<int:pk>/', views.coleta_detail, name='coleta_detail'),
    path('<int:pk>/editar/', views.coleta_edit, name='coleta_edit'),
    path('<int:coleta_id>/apagar-pneu/<int:pneu_id>/', views.apagar_pneu, name='apagar_pneu'),
]
