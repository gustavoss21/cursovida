from django.template import Library

register = Library()


@register.filter()
def ints(valor):
    print(1111111111, f'    {valor}')
    return [int(val) for val in valor]


@register.filter()
def carrinho_total(carrinho):
    if not type(carrinho) == str:
       return len(carrinho.values())
    else:
        return 0
