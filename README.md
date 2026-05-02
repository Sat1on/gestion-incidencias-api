# Sistema de Gestión de Incidencias

API REST desarrollada con Django y Django REST Framework para la gestión de incidencias.

## 🚀 Funcionalidades

- Crear incidencias
- Listar incidencias
- Editar incidencias
- Eliminar incidencias
- Panel de administración con Django Admin

## 🛠️ Tecnologías utilizadas

- Python
- Django
- Django REST Framework
- SQLite
- Git

## 📡 Endpoints principales

- GET /api/issues/
- POST /api/issues/
- PUT /api/issues/{id}/
- DELETE /api/issues/{id}/

## ▶️ Cómo ejecutar el proyecto

```bash
git clone https://github.com/Sat1on/gestion-incidencias-api.git
cd gestion-incidencias-api

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver