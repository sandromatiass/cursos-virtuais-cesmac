from django.shortcuts import render
from .models import Aluno, Curso

def lista_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'education/lista_alunos.html', {'alunos': alunos})

def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'education/lista_cursos.html', {'cursos': cursos})

def home(request):
    return render(request, 'education/home.html')
