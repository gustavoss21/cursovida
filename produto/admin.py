from django.contrib import admin
from .models import Produto, Categoria, Carrinho, MeusCursos

# Register your models here.


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'categoria', 'vendedo', 'slug')


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('categoria',)


@admin.register(Carrinho)
class CarrinhoAdmin(admin.ModelAdmin):
    list_display = ('produto', 'vendedor', 'preco', 'total')


@admin.register(MeusCursos)
class MeusCursosAdmin(admin.ModelAdmin):
    list_display = ('produto',)
