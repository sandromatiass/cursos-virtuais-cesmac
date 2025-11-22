# 🎓 Sistema Educacional CESMAC - Documentação do Projeto

## 📋 Sobre o Projeto

Sistema web desenvolvido em Django para gerenciamento de alunos e cursos, criado para atender instituições educacionais. A primeira versão inclui funcionalidades completas de CRUD para alunos e cursos, com interface administrativa personalizada.

## 🚀 Primeira Versão - Funcionalidades Implementadas

### ✅ Funcionalidades Principais

1. **Gestão de Alunos**
   - Cadastro com nome, sobrenome e email
   - Matrícula em múltiplos cursos
   - Listagem pública de alunos

2. **Gestão de Cursos** 
   - Cadastro com título e descrição
   - Associação de alunos matriculados
   - Listagem pública de cursos

3. **Interface Administrativa**
   - Painel admin personalizado com identidade visual
   - Navegação fixa entre páginas
   - Filtros e buscas avançadas

4. **Interface Pública**
   - Página inicial com dashboard
   - Listagens responsivas
   - Design moderno e profissional

## 🛠 Tecnologias Utilizadas

- **Backend:** Django 5.2.8
- **Frontend:** HTML5, CSS3, Font Awesome
- **Database:** SQLite (Desenvolvimento) / PostgreSQL (Produção)
- **Deploy:** Vercel + PostgreSQL

## 📁 Estrutura do Projeto

```
cursos-virtuais-cesmac/
├── backend/                 # Configurações do projeto Django
├── education/              # App principal
│   ├── models.py           # Modelos Aluno e Curso
│   ├── admin.py            # Configurações do admin
│   ├── views.py            # Views públicas
│   ├── urls.py             # URLs do app
│   └── templates/          # Templates organizados
├── vercel.json            # Configuração do Vercel
├── build_files.sh         # Script de build
├── requirements.txt       # Dependências Python
└── manage.py             # Gerenciador Django
```

## 🔧 Processo de Desenvolvimento - Versão 1.0

### Fase 1: Configuração Inicial ✅
- [x] Setup do projeto Django
- [x] Configuração do ambiente de desenvolvimento
- [x] Criação do app `education`

### Fase 2: Modelagem de Dados ✅
- [x] Definição do modelo `Aluno`
- [x] Definição do modelo `Curso` 
- [x] Relacionamento Many-to-Many entre Aluno e Curso
- [x] Migrações do banco de dados

### Fase 3: Interface Administrativa ✅
- [x] Registro dos modelos no admin
- [x] Personalização do Django Admin
- [x] Filtros e campos de busca
- [x] Interface personalizada com navegação fixa

### Fase 4: Views e Templates Públicos ✅
- [x] Página inicial com dashboard
- [x] Listagem de alunos
- [x] Listagem de cursos  
- [x] Templates responsivos e modernos
- [x] Navegação entre páginas

### Fase 5: Personalização e Estilo ✅
- [x] Identidade visual consistente
- [x] Ícones profissionais (Font Awesome)
- [x] Design responsivo
- [x] Experiência de usuário otimizada

### Fase 6: Preparação para Produção ✅
- [x] Configuração para deploy no Vercel
- [x] Setup do PostgreSQL
- [x] Configuração de static files
- [x] Variáveis de ambiente

## 🎯 Decisões de Arquitetura

### Modelagem de Dados
```python
# Relacionamento Many-to-Many otimizado
class Aluno(models.Model):
    cursos = models.ManyToManyField(Curso, related_name='alunos')
```

### Segurança
- Verificação de autenticação no admin
- Usuários staff para acesso administrativo
- Configurações seguras para produção

### UX/UI
- Navegação fixa para fácil acesso
- Ícones intuitivos
- Design consistente entre admin e site público

## 📊 Entregáveis da Versão 1.0

- [x] **Sistema completo de gestão educacional**
- [x] **Interface administrativa personalizada** 
- [x] **Site público funcional**
- [x] **Documentação técnica**
- [x] **Configuração para produção**


## 🚀 Como Executar o Projeto

### Desenvolvimento Local
```bash
# Clone o repositório
git clone <url-do-repositorio>
cd cursos-virtuais-cesmac

# Instale dependências
pip install -r requirements.txt

# Execute migrações
python manage.py migrate

# Crie superuser
python manage.py createsuperuser

# Execute o servidor
python manage.py runserver
```

### Produção (Vercel)
```bash
# Deploy automático via GitHub
# Ou usando Vercel CLI
vercel --prod
```

## 👥 Equipe e Contribuições

**Desenvolvido por:** Sandro Matias  
**Tecnologias:** Django, Python, HTML5, CSS3  
**Deploy:** Vercel + PostgreSQL

---

*Documentação atualizada em Novembro de 2025*  
*Sistema Educacional CESMAC - Versão 1.0*