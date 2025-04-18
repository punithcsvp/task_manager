# INDPRO Task Manager

A clean, modern Django-based Task Manager application with authentication, dashboards, and task management features , and CRUD operations.

##  Features

- User Signup / Login / Logout
- Task creation , Read , editing , and deletion
- Dashboard overview
- Beautiful, responsive UI with Html , Bootstrap 5 and custom styles

## Prerequest :
Download and Install python and set path in your envirnoment variables

Python installation :( https://www.python.org )

##  PROJECT SETUP

Follow these steps to set up the project :

### 1️⃣ Clone the Repository
 ## Go to your command Prompt :
 
   - Run the commands
 ```bash
 git clone [ https://github.com/punithcsvp/task_manager.git ]
 ```
```bash
 cd taskmanager
```
### 2️⃣ Create a Virtual Environment

**Windows :**

```bash
 python -m venv myenv
 myenv\Scripts\activate
```
**macOS / Linux :**

```bash
 python3 -m venv env
 source env/bin/activate
```
### 3️⃣ Install Dependencies

once the virtual envirnoment is activated ,run this command
```bash
pip install django
```
###  4️⃣ Run the Development Server

```bash
 python manage.py runserver
```
Open your browser and visit http://127.0.0.1:8000/ 🎉

---

## 📂 Project Structure

taskmanager/
├── taskmanager/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── tasks/
│   ├── migrations/
│   ├── static/
│   │   └── css/
│   │       └── styles.css
│   ├── templates/
│   │   ├── tasks/
│   │   │   ├── base.html
│   │   │   ├── dashboard.html
│   │   │   ├── login.html
│   │   │   ├── signup.html
│   │   │   ├── task_form.html
│   │   │   ├── task_list.html
│   │   │   └── view_task.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── db.sqlite3
└── manage.py


---


## 📸 Screenshots
 ## 1. LOGIN PAGE 
![1](https://github.com/user-attachments/assets/49d8a9e8-0590-4165-9b8d-515b99f6a950)

## 2. SignUp page
![2](https://github.com/user-attachments/assets/ddd5ba72-1848-4cdb-b220-e630e532ff95)

## 3. Task Page
![3](https://github.com/user-attachments/assets/80921cec-bb2e-4c20-98c8-a96b25c05744)

## 4. Create task
![4](https://github.com/user-attachments/assets/243a78cd-9f16-46a6-85d2-6488d2b7c626)

## 5. Dashboard
![5](https://github.com/user-attachments/assets/255739b5-d1ce-4b1c-8151-3fc17e62cd21)

## 6. Admin Page
![6](https://github.com/user-attachments/assets/21159f10-c492-47d5-8e9b-87876e0f4072)


## Assumptions Made During Development
- The system assumes that users must be authenticated to manage tasks (create, edit, delete).

- The front-end design is built using Html , css, Bootstrap 5 and custom CSS for simplicity and responsiveness.

- Static files are served locally during development without a CDN.

- The database used is SQLite3 for development purposes (easily portable and simple to set up).

---
## List of Technologies / Libraries Used
## Backend:
- Python 3

- Django 4.x

## Frontend:
- Html/css
- Bootstrap 5

## Font Awesome

- Google Fonts (Poppins)

- Custom CSS

## Tools:
- SQLite3 (for database)

- Virtual Environment (venv)

## 📃 License

This project is licensed under the MIT License.

---

##  My Github Account  
[https://github.com/punithcsvp/]

