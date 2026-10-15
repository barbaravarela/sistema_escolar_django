from django import forms

# ERRO ENCONTRADO: A classe Professor não foi importada corretamente.
# CORREÇÃO: Alterar o comando para from .models import Professor. O ponto (.) deve ser utilizado para indicar que o models.py que contém a classe Professor está na mesma pasta que este forms.py.
# from models import Professor
from .models import Professor

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['nome', 'sobrenome', 'email', 'telefone', 'registro',]
