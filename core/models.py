from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser,BaseUserManager


class UsuarioManage(BaseUserManager):
    user_in_migrations = True
    def _create_user(self,email,password, **extra_fields):
        if not email:
            raise ValueError(' O e-mail é obrigatorio')
        email = self.normalize_email(email)
        user = self.model(email=email,username=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)
        return self._create_user(email,password,**extra_fields)

    def create_superuser(self,email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if  extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ser is_superuser=True')

        if  extra_fields.get('is_staff') is not True:
            raise ValueError('Staff precisa ser is_staff=True')

        return self._create_user(email,password,**extra_fields)

class CustomUsuario(AbstractUser):
    email = models.EmailField('E-mail',unique=True)
    cpf = models.CharField('CPF',max_length=11)
    fone = models.CharField('Telefone',max_length=15)
    endereco = models.CharField('Endereço',max_length=15)
    is_staff = models.BooleanField('Membro da equipe',default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','cpf','fone','endereco']

    def __str__(self):
        return self.email

    objects = UsuarioManage()

class Base(models.Model):
    creado = models.DateField('Creado',auto_now_add=True)
    alterado = models.DateField('Atualizado',auto_now=True)
    ativo = models.BooleanField('Ativo',default=True)

    class Meta:
        abstract:True

class Vendedor(Base):
    usuario = models.ForeignKey('core.CustomUsuario',verbose_name='Usuário',on_delete=models.CASCADE,max_length=100)
    agenciador = models.CharField('Agenciador',max_length=100,default='')
    bio = models.CharField('Bio',max_length=100)

    class Meta:
        verbose_name = 'Vendedor'
        verbose_name_plural = 'Vendedores'

    def __str__(self):
        return self.agenciador