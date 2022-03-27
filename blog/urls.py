from cgitb import html
from django.urls import path, include
from .views import viewDetalhe, viewPrincipal, viewDelete, viewCriar, viewAlterar, viewCadastro, viewTabela

urlpatterns = [
    path("principal/", viewPrincipal, name = "principal"),
    path("postagem/<int:id>/", viewDetalhe, name = "detalhe"),
    path("deletar/<int:id>/", viewDelete, name = "delete"),
    path("criar-postagem", viewCriar, name = "criar"),
    path("alterar/<int:id>/", viewAlterar, name = "alterar"), 
    path("cadastro/", viewCadastro, name = "cadastro"),
    path("tabela/", viewTabela, name = "tabela"),

]
