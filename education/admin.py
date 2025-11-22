from django.contrib import admin
from .models import Aluno, Curso, Produto

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'sobrenome', 'email', 'quantidade_cursos', 'data_cadastro']
    list_filter = ['data_cadastro', 'cursos']
    search_fields = ['nome', 'sobrenome', 'email']
    filter_horizontal = ['cursos']
    ordering = ['nome']

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'duracao', 'preco', 'quantidade_alunos', 'data_criacao']
    list_filter = ['data_criacao']
    search_fields = ['titulo', 'descricao']
    ordering = ['titulo']

    def quantidade_alunos(self, obj):
        return obj.alunos.count()
    quantidade_alunos.short_description = 'Alunos'

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'preco', 'validade', 'esta_valido', 'data_criacao']
    list_filter = ['validade', 'data_criacao']
    search_fields = ['nome', 'descricao']
    ordering = ['nome']

admin.site.site_header = "Sistema Educacional CESMAC"
admin.site.site_title = "Admin CESMAC"
admin.site.index_title = "Bem-vindo ao Painel de Administração"