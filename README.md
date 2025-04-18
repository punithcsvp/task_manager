# INDPRO Task Manager

A clean, modern Django-based Task Manager application with authentication, dashboards, and task management features , and CRUD operations.

##  Features

- User Signup / Login / Logout
- Task creation , Read , editing , and deletion
- Dashboard overview
- Beautiful, responsive UI with Html , Bootstrap 5 and custom styles

##  PROJECT SETUP

Follow these steps to set up the project :

### 1️⃣ Clone the Repository

 -> git clone [ https://github.com/punithcsvp/task_manager.git ]

 -> cd taskmanager

### 2️⃣ Create a Virtual Environment

**Windows :**

-> python -m venv env
-> env\Scripts\activate

**macOS / Linux:**

python3 -m venv env
source env/bin/activate

### 3️⃣ Install Dependencies

pip install -r requirements.txt

> If you don't have a `requirements.txt`, you can create one:
pip freeze > requirements.txt

### 4️⃣ Apply Migrations

python manage.py migrate

### 5️⃣ Run the Development Server

python manage.py runserver

Open your browser and visit http://127.0.0.1:8000/ 🎉

---

## 📂 Project Structure

indpro-task-manager/
├── manage.py
├── requirements.txt
├── README.md
├── db.sqlite3
├── tasks/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
├── indpro_task_manager/
│   ├── settings.py
│   ├── urls.py
│   └── ...
└── ...

---

## 🔐 Environment Variables (Optional)

If needed, create a `.env` file for secret keys and settings:

SECRET_KEY=your-secret-key
DEBUG=True

You can load these using `python-decouple` or similar packages.

---

## 📸 Screenshots

*(Add screenshots of your login page, dashboard, and task list here)*

---

## 📃 License

This project is licensed under the MIT License.

---

## 👩‍💻 Author

Your Name  
https://github.com/yourusername

