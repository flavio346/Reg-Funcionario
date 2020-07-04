from django.shortcuts import render
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .models import Dados_Funcionario
from django.urls import reverse_lazy

# Create your views here.

class Lista_func(ListView):
    model = Dados_Funcionario
    template_name = 'lista.html'







class Detalhes(DetailView):
    model = Dados_Funcionario
    template_name = 'detal.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context



class Inserir(CreateView):
    model = Dados_Funcionario
    fields = ['Nome','Cpf','Idade','Data_de_Nascimento','Telefone','Email']
    template_name = 'formulario.html'
    success_url = reverse_lazy('listar')




class Atualizar(UpdateView):
    model = Dados_Funcionario
    fields = ['Nome','Cpf','Idade','Data_de_Nascimento','Telefone','Email']
    template_name = 'atual.html'
    success_url = reverse_lazy('listar')




class Apagar(DeleteView):
    model = Dados_Funcionario
    template_name = 'delete.html'
    success_url = reverse_lazy('listar')
