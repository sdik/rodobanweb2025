from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Tamanho
from .forms import TamanhoForm

# Create your views here.

class TamanhoListView(ListView):
    model = Tamanho
    template_name = 'tamanho/tamanho_list.html'
    context_object_name = 'tamanhos'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search', '')
        order = self.request.GET.get('order', 'medida')
        
        if search:
            queryset = queryset.filter(
                Q(medida__icontains=search)
            )
            
        if order.startswith('-'):
            queryset = queryset.order_by(order)
        else:
            queryset = queryset.order_by(order)
            
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '')
        context['current_order'] = self.request.GET.get('order', 'medida')
        return context

class TamanhoCreateView(CreateView):
    model = Tamanho
    form_class = TamanhoForm
    template_name = 'tamanho/tamanho_form.html'
    success_url = reverse_lazy('tamanho:tamanho_list')

class TamanhoUpdateView(UpdateView):
    model = Tamanho
    form_class = TamanhoForm
    template_name = 'tamanho/tamanho_form.html'
    success_url = reverse_lazy('tamanho:tamanho_list')

class TamanhoDeleteView(DeleteView):
    model = Tamanho
    template_name = 'tamanho/tamanho_confirm_delete.html'
    success_url = reverse_lazy('tamanho:tamanho_list')

class TamanhoDetailView(DetailView):
    model = Tamanho
    template_name = 'tamanho/tamanho_detail.html'
