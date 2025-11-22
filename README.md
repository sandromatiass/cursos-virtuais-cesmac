# 🎓 Sistema Educacional CESMAC

Sistema completo para gerenciamento de alunos, cursos e produtos desenvolvido em Django.

## ✨ Funcionalidades

### ✅ Implementadas
- **Gestão de Alunos** - Cadastro e listagem de alunos
- **Gestão de Cursos** - Cadastro e listagem de cursos  
- **Gestão de Produtos** - Cadastro e listagem de produtos
- **Interface Admin** - Painel administrativo completo
- **Formulários Web** - Cadastro de produtos via interface web
- **Templates Responsivos** - Interface moderna com Bootstrap
- **Banco de Dados** - SQLite (desenvolvimento) / PostgreSQL (produção)

### 🎯 Modelos do Sistema
- **Aluno** - nome, sobrenome, email, telefone, cursos (relacionamento)
- **Curso** - título, descrição, duração, preço
- **Produto** - nome, descrição, preço, validade

## 🚀 Como Executar

### Pré-requisitos
- Python 3.8+
- Django 5.2+
- PostgreSQL (opcional para produção)

### Instalação Local

1. **Clone o repositório**
```bash
git clone <repository-url>
cd cursos-virtuais-cesmac
```

2. **Configure ambiente virtual**
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

3. **Instale dependências**
```bash
pip install -r requirements.txt
```

4. **Configure variáveis de ambiente**
```env
# .env
SECRET_KEY=sua-chave-secreta-aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

5. **Execute migrações**
```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Crie superusuário**
```bash
python manage.py createsuperuser
```

7. **Execute servidor**
```bash
python manage.py runserver
```

## 🌐 Deploy no Vercel

### Configuração para Produção

1. **Variáveis de ambiente no Vercel:**
```env
SECRET_KEY=sua-chave-secreta-producao
DEBUG=False
ALLOWED_HOSTS=.vercel.app,.now.sh
DATABASE_URL=postgres://usuario:senha@host:porta/banco
```

2. **Arquivos de configuração:**
- `vercel.json` - Configuração do deploy
- `api/index.py` - Handler WSGI para Vercel
- `build_files.sh` - Script de build

### Estrutura do Projeto
```
cursos-virtuais-cesmac/
├── api/
│   └── index.py              # Handler Vercel
├── backend/
│   ├── settings.py           # Configurações
│   ├── urls.py               # URLs principais
│   └── wsgi.py               # WSGI application
├── education/
│   ├── models.py             # Modelos Aluno, Curso, Produto
│   ├── views.py              # Views do sistema
│   ├── forms.py              # Formulários
│   ├── admin.py              # Configuração Admin
│   ├── urls.py               # URLs da app
│   └── templates/            # Templates
├── requirements.txt          # Dependências
├── vercel.json              # Config Vercel
└── build_files.sh           # Script build
```

## 📊 URLs Disponíveis

| Rota | Descrição |
|------|-----------|
| `/` | Página inicial com estatísticas |
| `/admin/` | Painel administrativo Django |
| `/alunos/` | Lista de alunos cadastrados |
| `/cursos/` | Lista de cursos disponíveis |
| `/produtos/` | Lista de produtos cadastrados |
| `/produtos/novo/` | Formulário de novo produto |

## 🛠 Tecnologias Utilizadas

- **Backend:** Django 5.2.8
- **Database:** SQLite3 / PostgreSQL
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Deploy:** Vercel
- **Environment:** python-dotenv
- **Static Files:** WhiteNoise

## 📝 Desenvolvimento

### Comandos Úteis
```bash
# Criar migrações
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser

# Coletar arquivos estáticos
python manage.py collectstatic

# Verificar migrações
python manage.py showmigrations
```

### Estrutura de Desenvolvimento
- **Models:** `education/models.py`
- **Views:** `education/views.py` 
- **Forms:** `education/forms.py`
- **Templates:** `education/templates/education/`
- **Admin:** `education/admin.py`

## 🔧 Configuração de Produção

### Segurança
- DEBUG=False
- SECURE_SSL_REDIRECT=True
- CSRF_COOKIE_SECURE=True
- SESSION_COOKIE_SECURE=True

### Banco de Dados
- PostgreSQL no Supabase (Vercel)
- SQLite (desenvolvimento)


**Desenvolvido para o Sistema Educacional CESMAC** 🎓