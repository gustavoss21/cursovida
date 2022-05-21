from django.urls import path
from .views import ListaProdutoView, ListaFavoritosView, ApagarFavoritos, AdicionarFavoritos, Pesquisa


urlpatterns = [
    path('categoria/<int:pk>/', ListaProdutoView.as_view(), name='categoria'),
    path('favoritos/', ListaFavoritosView.as_view(), name='favoritos'),
    path('apagar-favoritos/',
         ApagarFavoritos.as_view(), name='apagar-favoritos'),
    path('adicionar-favoritos/', AdicionarFavoritos.as_view(),
         name='adicionar-favoritos'),
    path('pequisar/', Pesquisa.as_view(), name='pesquisar')
]
#
