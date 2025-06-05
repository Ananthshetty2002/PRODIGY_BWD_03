

### ✅ `README.md`

```markdown
# FastAPI JWT Authentication Example

A simple FastAPI project demonstrating user registration, login, and JWT-based authentication using `bcrypt` and `python-jose`.



## 🚀 Getting Started

### 1. Clone or create the folder

```bash
cd your_project_folder
````

### 2. Create and activate virtual environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the server

```bash
uvicorn app.main:app --reload
```

Server will start at:
**[http://127.0.0.1:8000](http://127.0.0.1:8000)**

Swagger UI:
**[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

---

## 🧪 API Endpoints (Postman/Swagger)

### 1. `POST /auth/register`

Create a new user.

**Body:**

```json
{
  "username": "john",
  "password": "secret123"
}
```

---

### 2. `POST /auth/login`

Login and receive an access token.

**Body:**

```json
{
  "username": "john",
  "password": "secret123"
}
```

**Response:**

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

---

### 3. `GET /auth/protected`

Protected route that requires a valid JWT token.

**Authorization:**

* Type: Bearer Token
* Value: `access_token` received from login

**Response:**

```json
{
  "message": "Hello john, you're authenticated!"
}
```

---

## 🛠 Tech Stack

* FastAPI
* Uvicorn
* bcrypt (password hashing)
* python-jose (JWT handling)
* passlib (hash utilities)

---

## 📌 Notes

* This project uses an in-memory DB (`fake_users_db`). For production, connect a real database like PostgreSQL or MongoDB.
* `SECRET_KEY` should be kept secret and stored securely.

