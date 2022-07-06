from cProfile import label
from http.client import HTTPResponse
from multiprocessing import get_context
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import View, DetailView, RedirectView, TemplateView, FormView
from django.views.generic.edit import CreateView
from datetime import datetime, timedelta
from django.contrib import messages
import json
from .form import MeusCursosForm
from django.urls import reverse_lazy
from .models import Produto, Categoria, MeusCursos
import re
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
        print(55555555,produto_id)
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
        # del self.request.session['carrinho']
        if not produto_id:
            return redirect(http_referer)
        else:
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
    template_name = 'detalhe.html'
    form_class = MeusCursosForm
    success_url = reverse_lazy('pagina-inicial')
    

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)

        http_referer = self.request.META.get('HTTP_REFERER',
                                             reverse('pagina-inicial'))
        produto_id = self.request.GET.get('pid')
        produto_or_carrinho = re.search(r'produto',produto_id)
        if not produto_id:
            return redirect(http_referer)
        if not produto_or_carrinho == None:
            produto_id = produto_id[:produto_or_carrinho.span()[0]-1]
            produto = get_object_or_404(Produto, nome=produto_id)
            nome = produto.nome
            preco = produto.preco
            vendedor = produto.vendedo
            id = produto.id
            imagem = produto.imagem
            imagem = imagem.name
            self.request.session['produto'] = {'nome': nome,
                                                            'preco': f'{preco}',
                                                            'vendedor': f'{vendedor}',
                                                            'imagem': imagem,
                                                            'id': id,
                                                            }

            context['produto'] = self.request.session.get('produto')
            context['produtos'] = []

            return context
        else:
            
            
            context['produtos'] = self.request.session.get('carrinho')
            context['produto'] = {}
            print('carrinho',self.request.session.get('carrinho'))
           
            return context
    
    def post(self,request,*args,**kwargs):
        print(0,request,1,*args,2,**kwargs)
        print(22222,self.request.POST)
        return super().post(request,*args,**kwargs)






    


