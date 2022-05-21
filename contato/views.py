from cgi import print_form
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import ContatoMessageForm
from django.contrib import messages


class ContatoView(FormView):

    template_name = 'contato.html'
    form_class = ContatoMessageForm
    success_url = reverse_lazy('pagina-inicial')

    def form_valid(self, form, *args, **kwargs):
        messages.success(self.request, 'Seu E-mail foi enviado com sucesso')
        form.send_mail()
        print(12334, 'formulario valido', 1111111111)

        return super(ContatoView, self).form_valid(form, * args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        print('error, 122345', form)
        messages.error(
            self.request, 'Seu E-mail não foi enviado, tente mais tarde')
        print(1111111111111222, 'formulario invalido')
        return super(ContatoView, self).form_invalid(form, *args, **kwargs)
