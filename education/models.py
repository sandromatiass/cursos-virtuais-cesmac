from django.db import models
from django.utils import timezone

class Curso(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título do Curso")
    descricao = models.TextField(verbose_name="Descrição")
    duracao = models.CharField(max_length=50, verbose_name="Duração", blank=True)
    preco = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name="Preço",
        blank=True, 
        null=True
    )
    data_criacao = models.DateTimeField(default=timezone.now)  

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ['titulo']

    def __str__(self):
        return self.titulo

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, blank=True)
    cursos = models.ManyToManyField(Curso, related_name='alunos', blank=True)
    data_cadastro = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"
        ordering = ['nome']

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"

    def quantidade_cursos(self):
        return self.cursos.count()
    quantidade_cursos.short_description = 'Cursos'

class Produto(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Produto")
    descricao = models.TextField(verbose_name="Descrição", blank=True)
    preco = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name="Preço"
    )
    validade = models.DateField(verbose_name="Data de Validade")
    data_criacao = models.DateTimeField(default=timezone.now)
    
    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ['nome']
    
    def __str__(self):
        return self.nome
    
    @property
    def esta_valido(self):
        return self.validade >= timezone.now().date()