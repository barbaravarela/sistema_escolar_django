from django.contrib import admin
from portal import models

@admin.register(models.Professor)
class ProfessorAdmin(admin.ModelAdmin):

    # ERRO ENCONTRADO: O campo 'especialidade' não existe na classe Professor.
    # CORREÇÃO: Trocar 'especialidade' por 'disciplina', já que este é o nome do atributo utilizado pela classe Professor para indicar a informação desejada.
    # list_display = ('id', 'nome', 'email', 'telefone', 'especialidade', 'ativo',)
    list_display = ('id', 'nome', 'email', 'telefone', 'disciplina', 'ativo',)

@admin.register(models.Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'telefone', 'ativo',)

@admin.register(models.Aula)
class AulaAdmin(admin.ModelAdmin):
    list_display = ('id', 'aluno_id', 'professor_id', 'status',)
