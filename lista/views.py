from unicodedata import name
from django.urls import reverse
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.shortcuts import HttpResponse, get_object_or_404, redirect
from requests import request, session
from django.contrib import messages
from produto.models import Produto, Categoria

# Create your views here.


class ListaProdutoView(DetailView):
    model = Categoria
    template_name = 'lista.html'
    pk_url_kwarg = "pk"
    context_object_name = 'categoria'


class AdicionarFavoritos(View):
    def get(self, *args, **kwargs):
        http_referer = self.request.META.get('HTTP_REFERER',
                                             reverse('carrinho'))
        print(111112345677, http_referer)
        if not self.request.user.is_authenticated:
            messages.info(
                self.request, 'para adicionar aos favoritos, primero faça login')
            return redirect('login')

        favoritos_id = self.request.GET.get('produto-id')
        if not favoritos_id:
            return redirect(http_referer)
        produto = get_object_or_404(Produto, id=favoritos_id)
        nome = produto.nome
        preco = produto.preco
        vendedor = produto.vendedo
        imagem = produto.imagem
        imagem = imagem.name
        # del self.request.session['favoritos']
        if not 'favoritos' in self.request.session:

            self.request.session['favoritos'] = {}
            self.request.session.save()

        if not favoritos_id in self.request.session['favoritos']:
            self.request.session['favoritos'][favoritos_id] = {'nome': nome,
                                                               'preco': f'{preco}',
                                                               'vendedor': f'{vendedor}',
                                                               'imagem': imagem,
                                                               'id': favoritos_id,
                                                               }
            messages.success(
                self.request, f'{nome} foi adicionado aos favoritos')
        else:
            messages.error(
                request=self.request, message=f'O curso de "{produto.nome}" já esta nos favoritos ')
        self.request.session.save()

        return redirect(http_referer)


class ApagarFavoritos(View):
    def get(self, *args, **kwargs):
        http_referer = self.request.META.get('HTTP_REFERER',
                                             reverse('pagina-inicial'))
        favoritos_id = self.request.GET.get('produto-id')

        # del self.request.session['carrinho']
        if not favoritos_id:
            messages.error(self.request, 'produto não existente no favoritos')
            return redirect(http_referer)
        else:
            nome = self.request.session['favoritos'][favoritos_id]['nome']
            messages.success(
                self.request, f'A remoção do {nome} foi bem sucedido!')
            del self.request.session['favoritos'][favoritos_id]

        self.request.session.save()
        return redirect(http_referer)


class ListaFavoritosView(TemplateView):
    template_name = 'favoritos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = self.request.session.get('favoritos')
        return context


class Pesquisa(TemplateView):
    template_name = 'pequisar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        produto = self.request.GET.get('pequisar')

        context['produtos'] = Produto.objects.filter(nome=produto)
        return context
