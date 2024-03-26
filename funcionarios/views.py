from django.shortcuts import render, redirect, get_object_or_404
from .models import Funcionario
from .forms import FuncionarioForm

def lista_funcionarios(request):
    funcionarios = Funcionario.objects.all()
    return render(request,'funcionarios/lista_funcionarios.html',{'funcionarios': funcionarios})
    
def cria_funcionario(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_funcionarios')
    else:
        form = FuncionarioForm()
    return render(request, 'funcionarios/cria_funcionario.html',{'form': form})

def edita_funcionario(request,pk):
    funcionarios = get_object_or_404(Funcionario, pk=pk)
    if request.method == 'POST':
        form = FuncionarioForm(request.POST, instance=funcionarios)
        if form.is_valid():
            form.save()
            return redirect('lista_funcionarios')
    else:
        form = FuncionarioForm(instance=funcionarios)
    return render(request,'funcionarios/edita_funcionario.html',{'form': form})

def deleta_funcionario(request, pk):
    funcionario = get_object_or_404(Funcionario, pk=pk)
    funcionario.delete()
    return redirect(lista_funcionarios)
    
