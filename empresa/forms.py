#recursos do Django de formularios
from django import forms

from .models import Assinante, Unidade, Safra, Cultura, Ccusto, Pcontas

"""Definir a classe utilizando o nome do modelo + Form.
   É necessario a classe meta para dizer a classe form quais campos serão
   reinderizados"""

class AssinanteForm(forms.ModelForm):
    class Meta:
        model = Assinante
        fields = '__all__'

class UnidadeForm(forms.ModelForm):
    class Meta:
        model = Unidade
        exclude = ['assinante']

class SafraForm(forms.ModelForm):
    class Meta:
        model = Safra
        exclude = ['assinante']

class CulturaForm(forms.ModelForm):
    class Meta:
        model = Cultura
        exclude = ['assinante']

class CcustoForm(forms.ModelForm):
    class Meta:
        model = Ccusto
        exclude = ['assinante']

class PcontasForm(forms.ModelForm):
    class Meta:
        model = Pcontas
        exclude = ['assinante']
