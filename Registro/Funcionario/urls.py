from django.contrib import admin
from django.urls import path
from .views import Lista_func
from .views import Detalhes
from .views import Inserir
from .views import Atualizar
from .views import Apagar

urlpatterns = [
    path('lista', Lista_func.as_view(), name="listar"),
    path('detail/<int:pk>/', Detalhes.as_view(), name="detal"),
    path('form', Inserir.as_view(), name="criar"),
    path('atualize/<int:pk>/', Atualizar.as_view(), name="editar" ),
    path('excluir/<int:pk>/', Apagar.as_view(), name="apague")
]


