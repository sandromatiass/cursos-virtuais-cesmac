from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import OperationalError

def home(request):
    context = {
        'total_alunos': 0,
        'total_cursos': 0,
        'total_produtos': 0,
    }

    try:
        from .models import Aluno
        context['total_alunos'] = Aluno.objects.count()
    except OperationalError:
        context['total_alunos'] = 0
    except:
        context['total_alunos'] = 0
        
    try:
        from .models import Curso
        context['total_cursos'] = Curso.objects.count()
    except OperationalError:
        context['total_cursos'] = 0
    except:
        context['total_cursos'] = 0
        
    try:
        from .models import Produto
        context['total_produtos'] = Produto.objects.count()
    except OperationalError:
        context['total_produtos'] = 0
    except:
        context['total_produtos'] = 0
        
    return render(request, 'education/home.html', context)

def lista_alunos(request):
    try:
        from .models import Aluno
        alunos = Aluno.objects.all()
    except OperationalError:
        alunos = []
        messages.info(request, "Tabela de alunos ainda não foi criada. Execute as migrações.")
    except:
        alunos = []
        
    return render(request, 'education/lista_alunos.html', {'alunos': alunos})

def lista_cursos(request):
    try:
        from .models import Curso
        cursos = Curso.objects.all()
    except OperationalError:
        cursos = []
        messages.info(request, "Tabela de cursos ainda não foi criada. Execute as migrações.")
    except:
        cursos = []
        
    return render(request, 'education/lista_cursos.html', {'cursos': cursos})

def lista_produtos(request):
    try:
        from .models import Produto
        produtos = Produto.objects.all()
    except OperationalError:
        produtos = []
        messages.info(request, "Tabela de produtos ainda não foi criada. Execute as migrações.")
    except:
        produtos = []
        
    return render(request, 'education/lista_produtos.html', {'produtos': produtos})

def produto_new(request):
    try:
        from .forms import ProdutoForm
        
        if request.method == 'POST':
            form = ProdutoForm(request.POST)
            if form.is_valid():
                produto = form.save()
                messages.success(request, f'Produto "{produto.nome}" cadastrado com sucesso!')
                return redirect('home')
        else:
            form = ProdutoForm()
            
    except OperationalError:
        messages.error(request, "Sistema de produtos não disponível. Execute as migrações primeiro.")
        return redirect('home')
    except Exception as e:
        messages.error(request, f"Erro ao acessar o formulário: {e}")
        return redirect('home')
    
    return render(request, 'education/produto_form.html', {'form': form})