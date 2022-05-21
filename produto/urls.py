from django.urls import path
from .views import ProdutoView, CarrinhoView, AdicionarCarrinho, ApagarCarrinho, MeusCursosAdicionar


urlpatterns = [
    path('carrinho/', CarrinhoView.as_view(), name='carrinho'),
    path('detalhe/<int:pk>/', ProdutoView.as_view(), name='detalhe'),
    path('adicionar-carrinho/', AdicionarCarrinho.as_view(),
         name='adicionar-carrinho'),
    path('remove-carrinho/', ApagarCarrinho.as_view(), name='remove-carrinho'),
    path('meus-cursos-adicionar/', MeusCursosAdicionar.as_view(),
         name='meus-cursos-adicionar'),

]
