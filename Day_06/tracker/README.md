# 🌟 Task Tracker API — FastAPI CRUD Project

A simple and efficient **FastAPI** project to manage Users and their Tasks with full **CRUD operations** and built-in validation using **Pydantic**. This project demonstrates how to design RESTful APIs using FastAPI and apply data validation, linking tasks to users.

---

## 📌 Features

✅ Create, Read, Update, and Delete **Users**  
✅ Create, Read, Update, and Delete **Tasks**  
✅ Link tasks to specific users  
✅ Filter tasks by user  
✅ Input validation with Pydantic  
✅ Auto-generated interactive docs (Swagger UI)

---

## 🧠 Technologies Used

- Python 3.9+
- FastAPI
- Pydantic
- Uvicorn (ASGI server)

---

## 🧩 Project Structure

task_tracker/
│
├── main.py # FastAPI routes
├── schemas.py # Pydantic models
├── crud.py # Business logic / operations

---

## 📥 Installation & Run

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/task-tracker-api
cd task-tracker-api
```

## 📥 Installation & Run

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install 'fastapi[standard]' pydantic
````

## 🔧 4. Run the Server

```bash
uvicorn main:app --reload
```

## 📂 Visit the Swagger Docs

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🧪 API Endpoints

### 👤 User Endpoints

| Method | Endpoint              | Description           |
|--------|-----------------------|-----------------------|
| POST   | `/users/`             | Create new user       |
| GET    | `/users/{id}`         | Get user by ID        |
| DELETE | `/users/{id}`         | Delete user by ID     |
| GET    | `/users/{id}/tasks`   | Get all tasks by user |

---

### ✅ Task Endpoints

| Method | Endpoint        | Description          |
|--------|------------------|----------------------|
| POST   | `/tasks/`        | Create new task      |
| GET    | `/tasks/{id}`    | Get task by ID       |
| PUT    | `/tasks/{id}`    | Update task status   |
| DELETE | `/tasks/{id}`    | Delete task by ID    |

---

## 📦 Sample JSON Payloads

### ➕ Create User

```json
{
  "username": "areeba",
  "email": "areeba@gmail.com"
}
```

### 📝 Create Task

```json
{
  "title": "Complete FastAPI Project",
  "description": "Task for learning CRUD",
  "due_date": "2025-06-15",
  "status": "pending",
  "user_id": 1
}
```

### 🔄 Update Task Status

```json
{
  "status": "completed"
}
```


## 🧑‍💻 Author

Made with ❤️ by **Areeba Zafar**  
🔗 GitHub — [AreebaZafarChohan](https://github.com/AreebaZafarChohan)

---

🔗 [MIT License](./LICENSE)
- Feel free to use and modify it as you wish!