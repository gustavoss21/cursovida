from django.template import Library

register = Library()


@register.filter
def valor_total(dicio):
    if not type(dicio) == str:
       return sum([float(valor['preco']) for valor in dicio.values()])
