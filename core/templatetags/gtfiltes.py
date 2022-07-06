from typing_extensions import Self
from django.template import Library
import re

register = Library()


@register.filter()
def ints(valor):
    return [int(val) for val in valor]


@register.filter()
def carrinho_total(carrinho):
    if not type(carrinho) == str:
       return len(carrinho.values())
    else:
        return 0
@register.filter()    
def for_filter(objetos,objeto):

    if objetos == None:
        return [objeto,]
    return objetos

@register.filter()
def filter_pid(valor):
    produto_or_carrinho = re.search(r'produto',valor)
    if not produto_or_carrinho == None:
        
        produto_id = valor[:produto_or_carrinho.span()[0]-1]
        return produto_id
        
    
    return valor

@register.filter()
def vai(opc,pid=None):
    print(11111,'filter',opc)
    print(11111,'filter',pid)

    return opc

