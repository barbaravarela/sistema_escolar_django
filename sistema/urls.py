from django.contrib import admin
from django.urls import path

from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),

    # ERRO ENCONTRADO: O mapeamento de cadastro/ está incorreto.
    # CORREÇÃO: Alterar o comando para path('', include('portal.urls')), já que cadastro/ é o path de uma url do app portal. Além disso, é preciso adicionar o comando from django.urls import include no início deste arquivo para que a função include() possa ser utilizada.
    # path('cadastro/', preciso mostrar a página cadastro.html),
    path('', include('portal.urls')),
]
