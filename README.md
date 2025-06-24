# 🧑‍💼 TeamTrack API

A simple Django REST API for managing employees and managers at an organization. Built for internship assignment purposes.

---

## 🚀 Features

- CRUD APIs for **Managers** and **Employees**
- Each employee is assigned to a single manager
- Get all employees under a specific manager
- Auto-documented using Swagger
- Hosted with HTTPS on [Railway](https://railway.app/)
- Built with Django + DRF + Uvicorn (ASGI)

---

## 📦 Tech Stack

- **Backend**: Django, Django REST Framework
- **ASGI Server**: Uvicorn
- **API Docs**: Swagger (drf-yasg)
- **Database**: SQLite (default), easy switch to PostgreSQL
- **Hosting**: Railway

---

## 📂 Project Structure

teamtrack/
├── core/ # App with models, views, serializers
├── teamtrack/ # Django settings
├── manage.py
├── requirements.txt
├── Procfile
└── README.md

yaml
Copy
Edit

---

## ⚙️ Setup Instructions (Local)

```bash
# Clone repo and enter folder
git clone https://github.com/your-username/teamtrack-api.git
cd teamtrack-api

# Setup virtual environment
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
