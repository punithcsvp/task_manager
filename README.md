# INDPRO Task Manager

A clean, modern Django-based Task Manager application with authentication, dashboards, and task management features , and CRUD operations.

##  Features

- User Signup / Login / Logout .
- Task creation , Read , editing , and deletion .
- Filter by categories , Complete/pending status , Title .
- Adding priority to the task.
- Dashboard overview .
- Beautiful, responsive UI with Html , Bootstrap 5 and custom styles .

## Prerequest :
Download and Install python and set path in your envirnoment variables

Python installation :( https://www.python.org )

## 1. PROJECT SETUP

Follow these steps to set up the project :

### 1️⃣ Clone the Repository
 ## Go to your command Prompt :
 
   - Run the commands
 ```bash
 git clone https://github.com/punithcsvp/task_manager.git  
 ```
```bash
 cd task_manager
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
## IMPLEMENTATION VIDEO
- Not able to run the project? No worries , heres a quick video how to implement
  
  https://github.com/user-attachments/assets/37fc41f2-b24c-41c4-87b7-9bca2e5233ba

## 2. Project Structure

taskmanager/
├── demo.gif              
├── taskmanager/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── tasks/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations/
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   ├── static/
│   │   │   └── css/
│   │   │       └── styles.css
│   │   ├── templates/
│   │       └── tasks/
│   │           ├── base.html
│   │           ├── dashboard.html
│   │           ├── login.html
│   │           ├── signup.html
│   │           ├── task_form.html
│   │           ├── task_list.html
│   │           └── view_task.html
├── db.sqlite3
├── manage.py
├── LICENSE
└── README.md


---
## Need the project demo? u got it! 
https://github.com/user-attachments/assets/50bdd972-3108-44b6-bfb7-1d2a9ec6bbf4a

## 3. Screenshots
 ## 1. LOGIN PAGE 
![8](https://github.com/user-attachments/assets/c30a7120-6c35-4bd6-a965-776e112cf876)

## 2. SignUp page
![9](https://github.com/user-attachments/assets/9e6464a6-07d9-400b-8069-af9528a8ed38)

## 3. Task Page
![3](https://github.com/user-attachments/assets/80921cec-bb2e-4c20-98c8-a96b25c05744)

## 4. Create task
![4](https://github.com/user-attachments/assets/243a78cd-9f16-46a6-85d2-6488d2b7c626)

## 5. Dashboard
![5](https://github.com/user-attachments/assets/255739b5-d1ce-4b1c-8151-3fc17e62cd21)

## 6. Admin Page
![10](https://github.com/user-attachments/assets/def9c7a1-8fb5-43d0-a79d-905520d7373c)


## 4. Assumptions Made During Development
- The system assumes that users must be authenticated to manage tasks (create, edit, delete).

- The front-end design is built using Html , css, Bootstrap 5 and custom CSS for simplicity and responsiveness.

- Static files are served locally during development without a CDN.

- The database used is SQLite3 for development purposes (easily portable and simple to set up).

---
## 5. List of Technologies / Libraries Used
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

---

## 6. Challenges Faced and How They Were Addressed
## 1. Designing a Clean, Modern UI

## Challenge :

Creating a visually appealing, user-friendly, and responsive design while keeping it simple.

## Solution :

Used Html,css,Bootstrap 5 with a customized color palette, gradients, and Google Fonts to enhance the UI/UX without adding heavy dependencies.

## 2. User Authentication & Session Handling

## Challenge :

Ensuring secure user authentication and managing login/logout workflows smoothly.

## Solution :

Implemented Django's built-in User authentication system, CSRF protection, and custom login/signup pages styled to match the application’s design.

## 3. Dynamic Layout Based on User State

## Challenge :

Displaying different navbar options and views based on whether the user is logged in or not.

## Solution :

Used Django template context processors and conditional rendering with {% if user.is_authenticated %} to dynamically adjust navigation and content.

---
## 📃 License

This project is licensed under the MIT License.

---

##  My Github Account  
[https://github.com/punithcsvp/]

