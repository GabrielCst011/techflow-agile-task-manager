```markdown
# TechFlow Agile Task Manager

## 🚀 Objetivo

Desenvolver um sistema básico de gerenciamento de tarefas usando metodologia ágil, permitindo:

- Acompanhar tarefas em tempo real
- Organizar fluxo de trabalho via Kanban
- Testar funcionalidades automaticamente

---
````
## 📦 Estrutura do Projeto
````
techflow-agile-task-manager/
│
├── src/
│ ├── app.py # Fábrica de app Flask
│ └── models.py # Modelos do banco (SQLAlchemy)
│
├── tests/
│ └── test_app.py # Testes unitários com pytest
│
├── docs/
│ └── diagramas/
│ ├── task_class.puml
│ └── task_usecase.puml
│
├── requirements.txt
├── .github/
│ └── workflows/
│ └── python-tests.yml
└── README.md

---

## ⚙️ Tecnologias

- **Python 3.10+**
- **Flask 2.3+**
- **Flask-SQLAlchemy 3.x**
- **SQLite** (local) / **PostgreSQL** (produção opcional)
- **Pytest 8.x** (testes unitários)
- **GitHub Actions** (CI/CD)

---

## 🔧 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/GabrielCst011/techflow-agile-task-manager.git
cd techflow-agile-task-manager
````

2. Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## 🏃‍♂️ Rodando localmente

```bash
python src/app.py
```

- O app rodará em: `http://127.0.0.1:5000`
- Endpoints disponíveis:

  - `GET /tasks` → Lista todas as tarefas
  - `POST /tasks` → Cria uma nova tarefa `{ "title": "Nome da tarefa" }`
  - `PUT /tasks/<id>` → Atualiza uma tarefa `{ "title": "...", "status": "..." }`
  - `DELETE /tasks/<id>` → Deleta uma tarefa

---

## ✅ Testes

O projeto utiliza **pytest** com **SQLite in-memory**:

```bash
pytest
```

- No GitHub Actions, os testes rodam automaticamente no workflow `.github/workflows/python-tests.yml`
- Todos os commits só serão considerados “verdinhos” se os testes passarem

---

## 📊 UML

- **Diagrama de Classes:** `docs/diagramas/task_class.puml`
- **Diagrama de Casos de Uso:** `docs/diagramas/task_usecase.puml`

---

## ⚡ Observações

- App estruturado com **fábrica de app** (`create_app()`) para compatibilidade com Flask 2.3+
- Testes criam e deletam tabelas explicitamente, evitando conflitos com `before_first_request`
- Estrutura preparada para produção com **PostgreSQL** ou qualquer outro banco suportado pelo SQLAlchemy

```

```
