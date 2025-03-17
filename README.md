# 📚 Libmanage - Library Management System

A simple web-based **Library Management System** built using **Django, MySQL, HTML, CSS, and JavaScript** for efficient book management and borrowing.

## 🚀 Features

- 🔐 **User Authentication** – Separate login for students and admins  
- 📖 **Book Management** – Admins can **add, edit, delete, and view books**  
- 📚 **Borrowing System** – Students can **borrow and view borrowed books**  
- 🎨 **Responsive UI** – Clean and user-friendly design  
- 🗄️ **Database Integration** – Uses **MySQL** for data storage  

## 🛠️ Tech Stack

- **Backend:** Django, Python, MySQL  
- **Frontend:** HTML, CSS, JavaScript  
- **Database:** MySQL  

## ⚙️ Installation

1️⃣ Clone the repository:
```sh
git clone https://github.com/Daksha10/libmanage.git
```

2️⃣ Navigate to the project directory:
```sh
cd library
```

3️⃣ Create and activate a virtual environment:
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

4️⃣ Install dependencies:
```sh
pip install -r requirements.txt
```

5️⃣ Apply database migrations:
```sh
python manage.py migrate
```

6️⃣ Create a superuser (admin):
```sh
python manage.py createsuperuser
```

7️⃣ Run the development server:
```sh
python manage.py runserver
```

8️⃣ Open the app in your browser:
```
http://127.0.0.1:8000/
```

## 📷 Screenshots

### 🔹 Login Page  
![Login Page](screenshots/loginpage.png)

### 🔹 Admin Dashboard  
![Admin Dashboard](screenshots/admin_dashboard.png)

### 🔹 Student Dashboard  
![Student Dashboard](screenshots/student_dashboard.png)
