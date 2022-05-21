from django.db import models
from stdimage.models import StdImageField
from django.db.models import signals
from django.template.defaultfilters import slugify

# Create your models here.


class Base(models.Model):
    creado = models.DateField('Creado', auto_now_add=True)
    alterado = models.DateField('Atualizado', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract: True


class Categoria(models.Model):
    categoria = models.CharField('Categoria', max_length=100)
    imagem = StdImageField('Imagem', null=True, upload_to='protutos', variations={
                           'thub': {'width': 39, 'height': 39, 'crop': True}})
    descricao = models.CharField(
        'Descrição curta', max_length=100)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.categoria


class Produto(Base):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    imagem = StdImageField('Imagem', null=True, upload_to='protutos', variations={
                           'thub': {'width': 200, 'height': 130, 'crop': True}})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)
    descricao_curta = models.CharField('Descrição curta', max_length=100)
    descricao_longa = models.TextField('Descrição longa', max_length=4000)
    categoria = models.ForeignKey(
        'produto.Categoria', verbose_name='Categoria', on_delete=models.CASCADE)
    vendedo = models.ForeignKey(
        'core.Vendedor', verbose_name='Vendedor', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.nome


def pro_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)


signals.pre_save.connect(pro_pre_save, sender=Produto)


class Carrinho(models.Model):
    produto = models.CharField('Produto', max_length=100)
    imagem = StdImageField('Imagem', upload_to='protutos', variations={
                           'thub': {'width': 150, 'height': 100, 'crop': True}})
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    sub_total = models.DecimalField('Subtotal', max_digits=8, decimal_places=2)
    vendedor = models.CharField('Vendedor', max_length=100)
    total = models.DecimalField('Total', max_digits=8, decimal_places=2)


class MeusCursos(models.Model):
    produto = models.ForeignKey(
        'produto.Produto', verbose_name='Produto', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Meu Curso'
        verbose_name_plural = 'Meus Cursos'

    def __str__(self):
        return self.produto
