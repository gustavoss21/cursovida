from calendar import c
import email
from this import d
from django import forms
from django.core.mail.message import EmailMessage


class ContatoMessageForm(forms.Form):
   nome = forms.CharField(label='Nome', max_length=100)
   email = forms.EmailField(label='E-mail', max_length=100)
   assunto = forms.CharField(label='Assunto', max_length=100)
   mensagem = forms.CharField(label='mensagem', widget=forms.Textarea())

   def send_mail(self):
       nome = self.cleaned_data['nome']
       mensagem = self.cleaned_data['mensagem']
       assunto = self.cleaned_data['assunto']
       email = self.cleaned_data['email']
       conteudo = f'Nome: {nome}\nE-mail: {email}\nassunto: {assunto}\n Mensagem: {mensagem}'
       mail = EmailMessage(
           subject=f'enviado por: {email}',
           body=conteudo,
           from_email='santos.gs708@gmail.com',
           headers={'reply-to': email, },
           to=['gustavosantos39738@gmail.com', ])
       print('123344dfdfdfw3  enviado com sucsss')
       mail.send()

# class ContatoForms(forms.Form):
#     def send_mail(self):
#         nome = self.cleaned_data['nome']
#         mensagem = self.cleaned_data['mensagem']
#         assunto = self.cleaned_data['assunto']
#         email = self.cleaned_data['email']
#         conteudo = f'Nome: {nome}\nE-mail: {email}\nassunto: {assunto}\n Mensagem: {mensagem}'
#         mail = EmailMessage(
#             subject=f'enviado por: {email}',
#             body=conteudo,
#             from_email='santos.gs708@gmail.com',
#             headers={'reply-to': email},
#             to=[email, ]
#         )

#         mail.send()
