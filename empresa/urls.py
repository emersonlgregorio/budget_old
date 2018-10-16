from django.urls import path

#importar todas as views
from . import views

"""
    toda a url no django é formada por um regex (expressão regular)
    toda url vai começar com "^" acompanhada com o que vai aparecer no navegador
    e termina com /$

    No segundo parametro, informamos para qual função será apontada a url

    O Terceiro parametro é o apelido da url.
"""
app_name = 'empresa'
urlpatterns = [
    path('novo-assinante/', views.novo_assinante, name='novo_assinante'),
    path('lista-assinante/', views.lista_assinante, name='lista_assinante'),
    path('nova-unidade/', views.nova_unidade, name='nova_unidade'),
    path('lista-unidade/', views.lista_unidade, name='lista_unidade'),
    path('nova-safra/', views.nova_safra, name='nova_safra'),
    path('nova-cultura/', views.nova_cultura, name='nova_cultura'),
    path('lista-cultura/', views.lista_cultura, name='lista_cultura'),
    path('novo-ccusto/', views.novo_ccusto, name='novo_ccusto'),
    path('novo-pcontas/', views.novo_pcontas, name='novo_pcontas'),
]
