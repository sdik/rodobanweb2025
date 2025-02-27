from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Produto
from .forms import ProdutoForm

# Create your views here.

class ProdutoListView(ListView):
    model = Produto
    template_name = 'produto/produto_list.html'
    context_object_name = 'produtos'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search', '')
        order = self.request.GET.get('order', 'descricao')
        
        if search:
            queryset = queryset.filter(
                Q(descricao__icontains=search) |
                Q(cod_bandag__icontains=search) |
                Q(grupo__icontains=search) |
                Q(subgrupo__icontains=search)
            )
            
        if order.startswith('-'):
            queryset = queryset.order_by(order)
        else:
            queryset = queryset.order_by(order)
            
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '')
        context['current_order'] = self.request.GET.get('order', 'descricao')
        return context

class ProdutoCreateView(CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produto/produto_form.html'
    success_url = reverse_lazy('produto:produto_list')

class ProdutoUpdateView(UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produto/produto_form.html'
    success_url = reverse_lazy('produto:produto_list')

class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'produto/produto_confirm_delete.html'
    success_url = reverse_lazy('produto:produto_list')

class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'produto/produto_detail.html'
