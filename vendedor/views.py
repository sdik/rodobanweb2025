from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Vendedor
from .forms import VendedorForm
from django.db.models import Q

class VendedorListView(LoginRequiredMixin, ListView):
    model = Vendedor
    template_name = 'vendedor/vendedor_list.html'
    context_object_name = 'vendedores'
    ordering = ['nome']  # ordenação padrão

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search', '')
        order = self.request.GET.get('order', 'nome')

        # Aplicar busca
        if search:
            queryset = queryset.filter(
                Q(nome__icontains=search) |
                Q(apelido__icontains=search) |
                Q(telefone__icontains=search)
            )

        # Aplicar ordenação
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

class VendedorCreateView(LoginRequiredMixin, CreateView):
    model = Vendedor
    form_class = VendedorForm
    template_name = 'vendedor/vendedor_form.html'
    success_url = reverse_lazy('vendedor:vendedor_list')

class VendedorUpdateView(LoginRequiredMixin, UpdateView):
    model = Vendedor
    form_class = VendedorForm
    template_name = 'vendedor/vendedor_form.html'
    success_url = reverse_lazy('vendedor:vendedor_list')

class VendedorDeleteView(LoginRequiredMixin, DeleteView):
    model = Vendedor
    template_name = 'vendedor/vendedor_confirm_delete.html'
    success_url = reverse_lazy('vendedor:vendedor_list')

class VendedorDetailView(LoginRequiredMixin, DetailView):
    model = Vendedor
    template_name = 'vendedor/vendedor_detail.html'
