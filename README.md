# ✅ Task Manager (Django)

A simple web-based Task Manager built with **Django**, **SQLite3**, and **HTML/CSS**. This app allows users to create, update, and delete tasks through a clean and responsive UI.

---

## 🚀 Features

- 📌 Add, edit, and delete tasks
- ✅ Mark tasks as completed or pending
- 📅 Sort and view task lists
- 🎨 Clean and responsive UI using HTML & CSS

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML5, CSS3 (with Django templates)
- **Database:** SQLite3

---

## 📁 Project Structure

taskmanager/
├── manage.py  
├── db.sqlite3  
├── myvenv/                # Virtual environment  
├── taskmanager/           # Project settings  
│   ├── __init__.py  
│   ├── settings.py  
│   ├── urls.py  
│   └── wsgi.py  
├── tasks/                 # App  
│   ├── migrations/  
│   ├── models.py  
│   ├── views.py  
│   ├── urls.py  
│   ├── templates/  
│   │   └── tasks/  
│   │       └── *.html  
│   ├── static/  
│   │   └── css/  
│   │       └── *.css  

---

## ⚙️ Getting Started

### 1. Clone the Repository

git clone https://github.com/your-username/task-manager.git  
cd task-manager

### 2. Create a Virtual Environment

python -m venv myvenv  
source myvenv/bin/activate  # Windows: myvenv\Scripts\activate

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Run Migrations

python manage.py migrate

### 5. Start the Server

python manage.py runserver

Visit `http://127.0.0.1:8000` in your browser to use the app.

---

## 📸 Screenshots

> _Add screenshots here if available (drag and drop into your README on GitHub)_

---

## 🧾 Requirements

Django>=3.2

You can regenerate it anytime using:

pip freeze > requirements.txt

---

## 👤 Author

- **Your Name**
- GitHub: [@your-username](https://github.com/your-username)

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.
