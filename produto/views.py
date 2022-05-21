from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import View, DetailView, RedirectView, TemplateView
from django.views.generic.edit import CreateView
from datetime import datetime, timedelta
from django.contrib import messages
import json
from .models import Produto, Categoria, MeusCursos
from django.shortcuts import get_object_or_404
# Create your views here.
# recursos estáticos
# https://www.w3schools.com/bootstrap5/index.php


class ProdutoView(DetailView):
    model = Produto
    template_name = 'produto.html'
    context_object_name = 'produto'
    pk_url_kwarg = "pk"


class AdicionarCarrinho(View):

    def get(self, *args, **kwargs):
        http_referer = self.request.META.get('HTTP_REFERER',
                                             reverse('pagina-inicial'))
        if not self.request.user.is_authenticated:
            messages.info(
                self.request, 'para adicionar ao carrinho, primero faça login')
            return redirect('login')

        produto_id = self.request.GET.get('pid')
        if not produto_id:
            return redirect(http_referer)
        produto = get_object_or_404(Produto, id=produto_id)
        nome = produto.nome
        preco = produto.preco
        vendedor = produto.vendedo
        imagem = produto.imagem
        imagem = imagem.name

        # del self.request.session['carrinho']
        if not 'carrinho' in self.request.session:

            self.request.session['carrinho'] = {}
            self.request.session.save()

        if not produto_id in self.request.session['carrinho']:
            self.request.session['carrinho'][produto_id] = {'nome': nome,
                                                            'preco': f'{preco}',
                                                            'vendedor': f'{vendedor}',
                                                            'imagem': imagem,
                                                            'id': produto_id,
                                                            }
            messages.success(
                self.request, f'{nome} foi adicionado ao carrinho')
        else:
            messages.error(
                request=self.request, message=f'O curso de "{produto.nome}" já esta no carrinho ')
        self.request.session.save()
        return redirect(http_referer)


class ApagarCarrinho(View):
    def get(self, *args, **kwargs):
        http_referer = self.request.META.get('HTTP_REFERER',
                                             reverse('pagina-inicial'))
        produto_id = self.request.GET.get('produto-id')
        print(1111111111111, '....', produto_id)
        # del self.request.session['carrinho']
        if not produto_id:
            return redirect(http_referer)
        else:
            ...
            # print('12345removido',
            #       self.request.session['carrinho'][produto_id])
            nome = self.request.session['carrinho'][produto_id]['nome']
            messages.success(
                self.request, f'A remoção do {nome} foi bem sucedido!')
            del self.request.session['carrinho'][produto_id]

            print(12345678, 'removido')
        self.request.session.save()
        return redirect(http_referer)


class CarrinhoView(TemplateView):
    template_name = 'carrinho.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CarrinhoView, self).get_context_data(*args, **kwargs)
        context['carrinho'] = self.request.session.get('carrinho')
        return context


class MeusCursosAdicionar(CreateView):
    model = MeusCursos
    template_name = 'pagina-inicial.html'
    fields = ['produto']
