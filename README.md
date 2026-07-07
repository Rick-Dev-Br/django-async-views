# Django Async Views

Projeto de estudo para o exercicio de Django Async Views.

## Como executar

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Depois acesse:

```text
http://127.0.0.1:8000/contador/
```

Para alterar o tempo do contador:

```text
http://127.0.0.1:8000/contador/?seconds=5
```

## Testes

```powershell
pytest
```
