from django.shortcuts import render

from .models import Curso


def index(request):
    context = {
        'desafio': 'Desafio FlipOn - Vitor Neodini Remedio',
        'descricao': 'Desenvolver uma página com um botão que leva até o currículo',
    }
    return render(request, 'index.html', context)


def contato(request):
    cursos = Curso.objects.all()
    context = {
        'cursos': cursos
    }
    return render(request, 'contato.html', context)


def curriculo(request):
    return render(request, 'curriculo.html')
