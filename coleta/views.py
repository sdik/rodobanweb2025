from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Coleta, PneusColeta
from .forms import ColetaForm, PneusColetaFormSet
from produto.models import Produto
from tamanho.models import Tamanho
from fabricante.models import Fabricante
from django.utils import timezone
from django.http import JsonResponse
import json
from django.db.models import Q, Sum

# Create your views here.

@login_required
def apagar_pneu(request, coleta_id, pneu_id):
    pneu = get_object_or_404(PneusColeta, pk=pneu_id, coleta_id=coleta_id)
    pneu.delete()
    messages.success(request, 'Pneu excluído com sucesso!')
    return redirect('coleta:coleta_edit', pk=coleta_id)

@login_required
def coleta_list(request):
    search_query = request.GET.get('search', '')
    sort_by = request.GET.get('sort', '-data')  # Default: ordenar por data mais recente
    
    coletas = Coleta.objects.select_related('cliente', 'vendedor').prefetch_related(
        'pneus__tamanho',
        'pneus__desenho',
        'pneus__fabricante'
    )
    
    if search_query:
        coletas = coletas.filter(
            Q(cliente__nome__icontains=search_query) |
            Q(cliente__nome_fantasia__icontains=search_query) |
            Q(cliente__razao_social__icontains=search_query) |
            Q(cliente__cpf__icontains=search_query) |
            Q(cliente__cnpj__icontains=search_query) |
            Q(vendedor__nome__icontains=search_query) 
        ).distinct()
    
    # Ordenação
    valid_sort_fields = {
        'data': 'data',
        '-data': '-data',
        'cliente': 'cliente__nome',
        '-cliente': '-cliente__nome',
        'vendedor': 'vendedor__nome',
        '-vendedor': '-vendedor__nome',
    }
    
    order_by = valid_sort_fields.get(sort_by, '-data')
    coletas = coletas.order_by(order_by)
    
    # Calculando o valor total dos pneus apenas somando o campo 'valor'
    coletas = coletas.annotate(
        valor_total_pneus=Sum('pneus__valor')
    )

    context = {
        'coletas': coletas,
        'search_query': search_query,
        'sort_by': sort_by,
        'current_date': timezone.now().date(),
    }
    return render(request, 'coleta/coleta_list.html', context)

@login_required
def coleta_detail(request, pk):
    coleta = get_object_or_404(Coleta, pk=pk)
    return render(request, 'coleta/coleta_detail.html', {'coleta': coleta})

@login_required
def coleta_new(request):
    if request.method == "POST":
        form = ColetaForm(request.POST)
        if form.is_valid():
            coleta = form.save(commit=False)
            coleta.data = timezone.now()
            coleta.save()
            
            # Processa os pneus
            total_forms = int(request.POST.get('pneuscoleta_set-TOTAL_FORMS', 0))
            print(f"Total de pneus a processar: {total_forms}")
            
            for i in range(total_forms):
                prefix = f'pneuscoleta_set-{i}-'
                print(f"Processando pneu {i + 1}:")
                print(f"Série: {request.POST.get(prefix + 'serie')}")
                print(f"Tamanho ID: {request.POST.get(prefix + 'tamanho')}")
                print(f"Desenho ID: {request.POST.get(prefix + 'desenho')}")
                print(f"Fabricante ID: {request.POST.get(prefix + 'fabricante')}")
                
                try:
                    PneusColeta.objects.create(
                        coleta=coleta,
                        serie=request.POST.get(prefix + 'serie'),
                        fogo=request.POST.get(prefix + 'fogo'),
                        tamanho_id=int(request.POST.get(prefix + 'tamanho')),
                        desenho_id=int(request.POST.get(prefix + 'desenho')),
                        fabricante_id=int(request.POST.get(prefix + 'fabricante')),
                        valor=float(request.POST.get(prefix + 'valor')),
                        montado=request.POST.get(prefix + 'montado') == 'true'
                    )
                    print(f"Pneu {i + 1} salvo com sucesso")
                except Exception as e:
                    print(f"Erro ao salvar pneu {i + 1}: {str(e)}")
                    messages.error(request, f'Erro ao salvar pneu {i + 1}: {str(e)}')
            
            messages.success(request, 'Coleta criada com sucesso!')
            return redirect('coleta:coleta_detail', pk=coleta.pk)
    else:
        form = ColetaForm()
    
    # Busca tamanhos ativos e produtos banda
    tamanhos = Tamanho.objects.filter(status='A')
    produtos_banda = Produto.objects.filter(grupo='B')
    fabricantes = Fabricante.objects.filter(status='A')
    
    context = {
        'form': form,
        'title': 'Nova Coleta',
        'tamanhos': tamanhos,
        'produtos_banda': produtos_banda,
        'fabricantes': fabricantes,
    }
    return render(request, 'coleta/coleta_form.html', context)

@login_required
def coleta_edit(request, pk):
    coleta = get_object_or_404(Coleta, pk=pk)
    if request.method == "POST":
        form = ColetaForm(request.POST, instance=coleta)
        if form.is_valid():
            coleta = form.save()
            
            # Processa os novos pneus
            total_forms = int(request.POST.get('pneuscoleta_set-TOTAL_FORMS', 0))
            print(f"Total de pneus a processar na edição: {total_forms}")
            
            for i in range(total_forms):
                prefix = f'pneuscoleta_set-{i}-'
                print(f"Processando pneu {i + 1} na edição:")
                print(f"Série: {request.POST.get(prefix + 'serie')}")
                print(f"Tamanho ID: {request.POST.get(prefix + 'tamanho')}")
                print(f"Desenho ID: {request.POST.get(prefix + 'desenho')}")
                print(f"Fabricante ID: {request.POST.get(prefix + 'fabricante')}")
                
                try:
                    PneusColeta.objects.create(
                        coleta=coleta,
                        serie=request.POST.get(prefix + 'serie'),
                        fogo=request.POST.get(prefix + 'fogo'),
                        tamanho_id=int(request.POST.get(prefix + 'tamanho')),
                        desenho_id=int(request.POST.get(prefix + 'desenho')),
                        fabricante_id=int(request.POST.get(prefix + 'fabricante')),
                        valor=float(request.POST.get(prefix + 'valor')),
                        montado=request.POST.get(prefix + 'montado') == 'true'
                    )
                    print(f"Pneu {i + 1} salvo com sucesso na edição")
                except Exception as e:
                    print(f"Erro ao salvar pneu {i + 1} na edição: {str(e)}")
                    messages.error(request, f'Erro ao salvar pneu {i + 1}: {str(e)}')
            
            messages.success(request, 'Coleta atualizada com sucesso!')
            return redirect('coleta:coleta_detail', pk=coleta.pk)
    else:
        form = ColetaForm(instance=coleta)
    
    # Busca tamanhos ativos e produtos banda
    tamanhos = Tamanho.objects.filter(status='A')
    produtos_banda = Produto.objects.filter(grupo='B')
    fabricantes = Fabricante.objects.filter(status='A')
    
    # Busca os pneus existentes
    pneus_existentes = list(coleta.pneus.all().values(
        'id', 'serie', 'fogo', 'tamanho_id', 'desenho_id', 
        'fabricante_id', 'valor', 'montado', 'garantia',
    ))
    
    context = {
        'form': form,
        'title': 'Editar Coleta',
        'tamanhos': tamanhos,
        'produtos_banda': produtos_banda,
        'fabricantes': fabricantes,
        'pneus_existentes': pneus_existentes,
        'coleta': coleta
    }
    return render(request, 'coleta/coleta_form.html', context)
