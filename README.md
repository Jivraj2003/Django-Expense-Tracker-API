
# 💸 Django Expense Tracker API

A RESTful backend API built with Django and Django REST Framework to manage personal income and expenses, with JWT-based user authentication. Developed as part of an internship task.

---

## 🚀 Features

- 🔐 JWT Authentication (Login, Refresh)
- 👤 User Registration
- 💰 Track Expenses and Incomes (CRUD)
- 💸 Flat and Percentage-Based Tax Calculation
- 📊 Pagination for Lists
- 🔐 Access Control (Regular Users vs Superusers)
- 📎 RESTful Endpoints

---

## 🛠 Tech Stack

- **Backend**: Django, Django REST Framework
- **Authentication**: JWT via `djangorestframework-simplejwt`
- **Database**: SQLite (dev mode)
- **Language**: Python 3.8+
- **Tools**: Postman, DRF Browsable API

---

## 📦 Installation

### 1. Clone the Repo

```bash
git clone https://github.com/Jivraj2003/Django-Expense-Tracker-API.git
cd Django-Expense-Tracker-API
```

### 2. Create Virtual Environment

```bash
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, install manually:

```bash
pip install django djangorestframework djangorestframework-simplejwt
```

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 6. Run Development Server

```bash
python manage.py runserver
```

---

## 🔐 Authentication (JWT)

### Register

```http
POST /api/auth/register/
```

**Body:**
```json
{
  "username": "testuser",
  "password": "testpass123"
}
```

### Login

```http
POST /api/auth/login/
```

**Response:**
```json
{
  "access": "jwt-access-token",
  "refresh": "jwt-refresh-token"
}
```

### Refresh

```http
POST /api/auth/refresh/
```

**Body:**
```json
{
  "refresh": "jwt-refresh-token"
}
```

Use `access` token for protected endpoints in headers:

```
Authorization: Bearer <access-token>
```

---

## 📚 API Endpoints

### 🔑 Auth Endpoints

| Method | URL                     | Description         |
|--------|-------------------------|---------------------|
| POST   | /api/auth/register/     | Register a user     |
| POST   | /api/auth/login/        | Login, get JWT      |
| POST   | /api/auth/refresh/      | Refresh JWT         |

### 💰 Expense/Income Endpoints

| Method | URL                    | Description              |
|--------|------------------------|--------------------------|
| GET    | /api/expenses/         | List user’s records      |
| POST   | /api/expenses/         | Create a new record      |
| GET    | /api/expenses/{id}/    | View specific record     |
| PUT    | /api/expenses/{id}/    | Update specific record   |
| DELETE | /api/expenses/{id}/    | Delete specific record   |

---

## 🧮 Tax Calculation

| Tax Type | Logic                          |
|----------|---------------------------------|
| flat     | `total = amount + tax`         |
| percentage | `total = amount + (amount * tax / 100)` |

---

## 🛡 Permissions

| User Type     | Permissions                          |
|---------------|--------------------------------------|
| Regular User  | Can only access their own records    |
| Superuser     | Can access all users' records        |
| Anonymous     | Cannot access protected endpoints    |

---

## 🧪 Testing

You can use Postman or the Django REST Framework web interface to test:

- ✅ Register & Login via `/api/auth/`
- ✅ Copy `access` token and test endpoints
- ✅ CRUD operations with `/api/expenses/`
- ✅ Test tax logic (flat & percentage)
- ✅ Use superuser to view all records

---

## 📁 Project Structure

```
expense_tracker/
├── tracker/                # Main app
│   ├── models.py           # Data models
│   ├── views.py            # API views
│   ├── serializers.py      # Data serializers
│   ├── urls.py             # App-specific URLs
├── expense_tracker/        # Project config
│   ├── settings.py         # Project settings
├── manage.py               # Django entry point
```

---

## 📬 License

MIT License. Use it for learning and development.

---

## 💬 Feedback

Pull requests and suggestions are welcome!  
Feel free to fork, modify, and build on top of this.
