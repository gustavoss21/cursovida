from dataclasses import fields
import imp
from .models import MeusCursos, Produto
from django.forms import ModelForm

class MeusCursosForm(ModelForm):
    produtos = '123'
    class Meta:
         model = MeusCursos
         fields = ('produto',)
         