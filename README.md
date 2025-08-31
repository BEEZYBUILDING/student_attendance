```markdown
# 🎓 Student Attendance Tracking API

A **Django + Django REST Framework (DRF)** project for tracking classroom attendance.  
It allows administrators/teachers to manage **students, classrooms, and attendance records** with secure token-based authentication.

---

## 🚀 Features

- ✅ Manage **Students** (CRUD)
- ✅ Manage **Classrooms** (CRUD)
- ✅ Track **Attendance Records** (Present / Absent / Late)
- ✅ Token-based authentication (JWT)
- ✅ Interactive API Documentation (Swagger + Redoc)
- ✅ Admin Panel for quick management

---

## 🛠 Tech Stack

- [Python 3.13+](https://www.python.org/)
- [Django 5.x](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
- [drf-yasg](https://drf-yasg.readthedocs.io/) (Swagger Docs)

---

## 📂 Project Structure

```

attendance\_app/
├── student\_attendance/
│   ├── attendance/          # App with models, views, serializers
│   ├── migrations/
│   ├── urls.py              # API routes
│   └── ...
├── manage.py
└── README.md

````

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repo
```bash
git clone https://github.com/your-username/attendance_app.git
cd attendance_app
````

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
# or
source venv/bin/activate   # On Mac/Linux
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run migrations

```bash
python manage.py migrate
```

### 5️⃣ Create a superuser

```bash
python manage.py createsuperuser
```

### 6️⃣ Run the server

```bash
python manage.py runserver
```

---

## 🔑 Authentication (JWT)

1. Get a token:

   ```http
   POST /api/token/
   {
     "username": "your_username",
     "password": "your_password"
   }
   ```

   Response:

   ```json
   {
     "access": "your_access_token",
     "refresh": "your_refresh_token"
   }
   ```

2. Use token in requests:

   ```
   Authorization: Bearer your_access_token
   ```

---

## 📌 API Endpoints

| Resource   | Method | Endpoint              | Description             |
| ---------- | ------ | --------------------- | ----------------------- |
| Students   | GET    | `/api/students/`      | List all students       |
|            | POST   | `/api/students/`      | Add a new student       |
|            | GET    | `/api/students/{id}/` | Retrieve a student      |
|            | PUT    | `/api/students/{id}/` | Update a student        |
|            | DELETE | `/api/students/{id}/` | Delete a student        |
| Classrooms | GET    | `/api/classrooms/`    | List all classrooms     |
| Attendance | GET    | `/api/attendance/`    | List attendance records |
| Auth       | POST   | `/api/token/`         | Get JWT token           |
|            | POST   | `/api/token/refresh/` | Refresh token           |

---

## 📖 API Documentation

* Swagger UI → [http://127.0.0.1:8000/api/schema/swagger-ui/](http://127.0.0.1:8000/api/schema/swagger-ui/)
* Redoc → [http://127.0.0.1:8000/api/schema/redoc/](http://127.0.0.1:8000/api/schema/redoc/)

---

## 🔍 Testing

* Visit **Swagger UI** and test endpoints interactively.
* Or use **Django Admin** at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).
* Or use **Postman / cURL** to send requests with JWT tokens.

---

## 🤝 Contributing

1. Fork this repo
2. Create a new branch (`feature/my-feature`)
3. Commit your changes (`git commit -m "Added my feature"`)
4. Push to your branch (`git push origin feature/my-feature`)
5. Open a Pull Request 🎉

---

## 📜 License

This project is open-source under the **MIT License**.
