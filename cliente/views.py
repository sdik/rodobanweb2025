from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Cliente
from .forms import ClienteForm
from django.db.models import Q, Value, CharField
from django.db.models.functions import Coalesce

# Create your views here.

class ClienteListView(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = 'cliente/cliente_list.html'
    context_object_name = 'clientes'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Adiciona um campo nome_completo que combina nome/razao_social
        queryset = queryset.annotate(
            nome_completo=Coalesce('nome', 'razao_social')
        )
        
        # Busca
        search = self.request.GET.get('search', '')
        if search:
            queryset = queryset.filter(
                Q(nome__icontains=search) |
                Q(razao_social__icontains=search) |
                Q(cpf__icontains=search) |
                Q(cnpj__icontains=search)
            )
        
        # Ordenação
        order_by = self.request.GET.get('order_by', 'nome_completo')
        direction = self.request.GET.get('direction', 'asc')
        
        if direction == 'desc':
            order_by = f'-{order_by}'
            
        if order_by.replace('-', '') in ['nome_completo', 'tipo_pessoa', 'cpf', 'cnpj', 'telefone']:
            queryset = queryset.order_by(order_by)
            
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_order_by'] = self.request.GET.get('order_by', 'nome_completo')
        context['current_direction'] = self.request.GET.get('direction', 'asc')
        return context

class ClienteCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/cliente_form.html'
    success_url = reverse_lazy('cliente:cliente_list')
    success_message = 'Cliente cadastrado com sucesso!'

class ClienteUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/cliente_form.html'
    success_url = reverse_lazy('cliente:cliente_list')
    success_message = 'Cliente atualizado com sucesso!'

class ClienteDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Cliente
    template_name = 'cliente/cliente_confirm_delete.html'
    success_url = reverse_lazy('cliente:cliente_list')
    success_message = 'Cliente excluído com sucesso!'

class ClienteDetailView(LoginRequiredMixin, DetailView):
    model = Cliente
    template_name = 'cliente/cliente_detail.html'
