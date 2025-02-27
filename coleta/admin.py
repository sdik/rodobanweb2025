from django.contrib import admin
from .models import Coleta, PneusColeta

# Register your models here.

class PneusColetaInline(admin.TabularInline):
    model = PneusColeta
    extra = 1

@admin.register(Coleta)
class ColetaAdmin(admin.ModelAdmin):
    list_display = ['numero_apanha', 'data', 'cliente', 'vendedor', 'forma_pagamento']
    list_filter = ['data', 'forma_pagamento']
    search_fields = ['numero_apanha', 'cliente__nome', 'vendedor__nome']
    inlines = [PneusColetaInline]

@admin.register(PneusColeta)
class PneusColetaAdmin(admin.ModelAdmin):
    list_display = ['coleta', 'serie', 'fogo', 'tamanho', 'desenho', 'valor', 'montado']
    list_filter = ['montado', 'tamanho', 'fabricante']
    search_fields = ['serie', 'fogo', 'coleta__numero_apanha']
