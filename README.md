## SISTEMA ESCOLAR DJANGO

# DESCRIÇÃO DO PROJETO

O projeto consiste no desenvolvimento de um sistema escolar utilizando o framework Django, com o objetivo de gerenciar as informações de professores, alunos e aulas. A aplicação permite organizar os dados desses elementos por meio de modelos, formulários, visualizações e rotas, integrando as funcionalidades do sistema ao banco de dados. Entretanto, o projeto apresenta oito erros distribuídos em diferentes arquivos, que precisam ser identificados e corrigidos para garantir o funcionamento adequado da aplicação.

# LISTA DOS OITO ERROS

`Erro 1: portal/models.py`
ERRO ENCONTRADO: A função timezone.now() não está sendo reconhecida, pois o módulo timezone do django.utils não foi importado.
CORREÇÃO: Adicionar o comando from django.utils import timezone no início do arquivo para que a função possa ser utilizada.

`Erro 2: portal/models.py`
ERRO ENCONTRADO: A matrícula é o identificador do aluno e, portanto, deve ser único.
CORREÇÃO: Adicionar unique=True entre os parênteses de models.IntegerField para garantir que não haverá duplicidade de matrículas.

`Erro 3: portal/views.py`
ERRO ENCONTRADO: O caminho para o arquivo index.html está incorreto.
CORREÇÃO: Alterar o caminho para 'portal/index.html'. Essa é a opção correta, pois quando o render() é utilizado o Django já sabe que deve inciar a procura pelo arquivo na pasta templates.

`Erro 4: portal/forms.py`
ERRO ENCONTRADO: A classe Professor não foi importada corretamente.
CORREÇÃO: Alterar o comando para from .models import Professor. O ponto (.) deve ser utilizado para indicar que o models.py que contém a classe Professor está na mesma pasta que este forms.py.

`Erro 5: portal/admin.py`
ERRO ENCONTRADO: O campo 'especialidade' não existe na classe Professor.
CORREÇÃO: Trocar 'especialidade' por 'disciplina', já que este é o nome do atributo utilizado pela classe Professor para indicar a informação desejada.

`Erro 6: portal/urls.py`
ERRO ENCONTRADO: O mapeamento de cadastro/ não funciona, pois a view cadastro não existe em views.py.
CORREÇÃO: Criar a view cadastro em views.py. Além disso, como ela utilizará HttpResponse, é necessário adicionar o comando from django.htpp import HttpResponse no início de views.py.

`Erro 7: sistema/urls.py`
ERRO ENCONTRADO: O mapeamento de cadastro/ está incorreto.
CORREÇÃO: Alterar o comando para path('', include('portal.urls')), já que cadastro/ é o path de uma url do app portal. Além disso, é preciso adicionar o comando from django.urls import include no início deste arquivo para que a função include() possa ser utilizada.

`Erro 8: sistema/settings.py`
ERRO ENCONTRADO: O app portal não foi adicionado na lista INSTALLED_APPS, então ele não é reconhecido.
CORREÇÃO: Adicionar 'portal',

# COMO RODAR O PROJETO LOCALMENTE

1. Abra o cmd do VS Code (ctrl + aspas)
2. Caso o Django não esteja instalado execute o comando pip install django
3. Caso o Pillow não esteja instalado execute o comando pip install Pillow
4. Execute o comando: python manage.py runserver
5. Acesse o servidor no navegador (ctrl + clique no endereço http que aparecer)

OBS.: O super usuário criado é root e a senha é 12345.

# INTEGRANTES DO GRUPO

Barbara Varela Bonfim, Lídia Sales Sena e Samara de Jesus Gomes
