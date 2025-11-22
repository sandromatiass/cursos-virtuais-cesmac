from django.contrib import admin
from .models import Aluno, Curso

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'sobrenome', 'email', 'quantidade_cursos']
    list_filter = ['cursos']
    search_fields = ['nome', 'sobrenome', 'email']
    filter_horizontal = ['cursos'] 
    
    def quantidade_cursos(self, obj):
        return obj.cursos.count()
    quantidade_cursos.short_description = 'Cursos'

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'quantidade_alunos']
    search_fields = ['titulo']

    
    def quantidade_alunos(self, obj):
        return obj.alunos.count()
    quantidade_alunos.short_description = 'Alunos'

admin.site.site_header = "Sistema Educacional CESMAC"
admin.site.site_title = "Admin CESMAC"
admin.site.index_title = "Bem-vindo ao Painel de Administração"