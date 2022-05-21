from django.urls import path
from .views import IndexView, Cadastro


urlpatterns = [
    path('', IndexView.as_view(), name='pagina-inicial'),
    path('cadastro/', Cadastro.as_view(), name='cadastro'),

]
#
