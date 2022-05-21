from telnetlib import LOGOUT
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from requests import request
from produto.models import Produto, Categoria, MeusCursos
from django.shortcuts import get_object_or_404
from .forms import CustomUsuarioCreateForm


class IndexView(TemplateView):
    template_name = 'pagina-inicial.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['produtos'] = Produto.objects.all()
        produtos = Produto.objects.all()
        context['categorias'] = Categoria.objects.all()
        context['meus-cursos'] = MeusCursos.objects.all()
        print(self)
        # tirar todas as categorias vazias, ou seja, as que nao estao na categoria do produto
        lista = []
        for categoria1 in context['categorias']:
            for produto in context['produtos']:
                if f'{categoria1.categoria}' == f'{produto.categoria}':
                    lista.append(categoria1)
        lista = set(lista)
        context['categorias'] = list(lista)
        # ###### end ###### #

        return context


class Cadastro(FormView):

    template_name = 'cadastro.html'
    form_class = CustomUsuarioCreateForm
    success_url = reverse_lazy('login')

    def form_valid(self, form, *args, **kwargs):
        form_class = super(Cadastro, self).form_class

        self.form_class.save(form, commit=True)
        messages.add_message(self.request, messages.SUCCESS,
                             ' agora pode fazer login')
        return super(Cadastro, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):

        messages.add_message(self.request, messages.ERROR,
                             ' ouve um erro no cadastro')
        return super(Cadastro, self).form_invalid(form, *args, **kwargs)
