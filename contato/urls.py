from django.urls import path
from .views import ContatoView


urlpatterns = [
    path('contato/', ContatoView.as_view(), name='contato'),
]
