from django.urls import path

from portal import views

urlpatterns = [
    path('index/', views.index),

    # ERRO ENCONTRADO: O mapeamento de cadastro/ não funciona, pois a view cadastro não existe em views.py.
    # CORREÇÃO: Criar a view cadastro em views.py. Além disso, como ela utilizará HttpResponse, é necessário adicionar o comando from django.htpp import HttpResponse no início de views.py.
    path('cadastro/', views.cadastro),
]
