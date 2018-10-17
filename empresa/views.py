from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse

from .forms import AssinanteForm, UnidadeForm, SafraForm, CulturaForm
from .forms import CcustoForm, PcontasForm

from .models import Assinante, Cultura, Unidade, Safra, Ccusto, Pcontas

# formulario Assinante
def novo_assinante(request):
    if request.method == 'POST':
        form = AssinanteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Assinante Adicionado!')
        else:
            print(form.errors)
    else:
        form = AssinanteForm ()
    return render(request, 'empresa/novo_assinante.html', {'form':form})

def lista_assinante(request):
    assinante = Assinante.objects.all()
    return render(request, 'empresa/lista_assinante.html', {'assinante': assinante})

#Formulario Unidade
def nova_unidade(request):
    if request.method == 'POST':
        form = UnidadeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('empresa:lista_unidade')
        else:
            print(form.errors)
    else:
        form = UnidadeForm()
    return render(request, 'empresa/form_unidade.html', {'form':form})

def lista_unidade(request):
    unidade = Unidade.objects.all()
    return render(request, 'empresa/lista_unidade.html', {'unidade': unidade})

#Formulario Safra
def nova_safra(request):
    if request.method == 'POST':
        form = SafraForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Safra Adicionada!!')
        else:
            print(form.errors)
    else:
        form = SafraForm()
    return render (request, 'empresa/form_safra.html', {'form':form})

def lista_safra(request):
    safra = Safra.objects.all()
    return render(request, 'empresa/lista_safra.html', {'safra':safra})

#Formulario Cultura
def nova_cultura(request):
    if request.method == 'POST':
        form = CulturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('empresa:lista_cultura')
        else:
            print(form.errors)
    else:
        form = CulturaForm()
    return render(request, 'empresa/form_cultura.html', {'form':form})

def lista_cultura(request):
    cultura = Cultura.objects.all()
    return render(request, 'empresa/lista_cultura.html', {'cultura': cultura})

#Formulario Centro de Custo
def novo_ccusto(request):
    if request.method == 'POST':
        form = CcustoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Centro de custo adicionado!')
        else:
            print(form.errors)
    else:
        form = CcustoForm()
    return render(request, 'empresa/form_ccusto.html', {'form':form})

#Formulario Plano de Contas
def novo_pcontas(request):
    if request.method == 'POST':
        form = PcontasForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Conta adcionada com sucesso')
        else:
            print(form.errors)
    else:
        form = PcontasForm()
    return render(request, 'empresa/form_pcontas.html', {'form':form})
