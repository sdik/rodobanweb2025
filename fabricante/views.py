from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Fabricante
from .forms import FabricanteForm

# Create your views here.

class FabricanteListView(ListView):
    model = Fabricante
    template_name = 'fabricante/fabricante_list.html'
    context_object_name = 'fabricantes'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search', '')
        order = self.request.GET.get('order', 'nome')
        
        if search:
            queryset = queryset.filter(
                Q(nome__icontains=search)
            )
            
        if order.startswith('-'):
            queryset = queryset.order_by(order)
        else:
            queryset = queryset.order_by(order)
            
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '')
        context['current_order'] = self.request.GET.get('order', 'nome')
        return context

class FabricanteCreateView(CreateView):
    model = Fabricante
    form_class = FabricanteForm
    template_name = 'fabricante/fabricante_form.html'
    success_url = reverse_lazy('fabricante:fabricante_list')

class FabricanteUpdateView(UpdateView):
    model = Fabricante
    form_class = FabricanteForm
    template_name = 'fabricante/fabricante_form.html'
    success_url = reverse_lazy('fabricante:fabricante_list')

class FabricanteDeleteView(DeleteView):
    model = Fabricante
    template_name = 'fabricante/fabricante_confirm_delete.html'
    success_url = reverse_lazy('fabricante:fabricante_list')

class FabricanteDetailView(DetailView):
    model = Fabricante
    template_name = 'fabricante/fabricante_detail.html'
