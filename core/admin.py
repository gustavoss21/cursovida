from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUsuarioCreateForm,CustomUsuarioChangeForm
from .models import CustomUsuario,Vendedor
# Register your models here.



@admin.register(Vendedor)
class VendedorAdmin(admin.ModelAdmin):
    list_display = ('agenciador','usuario')

@admin.register(CustomUsuario)
class CustomUsuarioAdmin(UserAdmin):
    add_form = CustomUsuarioCreateForm
    list_display_links = ('email',)
    form = CustomUsuarioChangeForm
    model = CustomUsuario
    list_display = ('first_name','last_name','cpf','email','is_staff')
    fieldsets = (
                 (None,{'fields':('email','password')}),
                 ('Informações pessoais',{'fields':('first_name','last_name','cpf','fone','endereco')}),
                 ('Permissões',{'fields':('is_active','is_staff','is_superuser','groups','user_permissions')}),
                 ('Datas importantes',{'fields':('last_login','date_joined')}),
                 )


