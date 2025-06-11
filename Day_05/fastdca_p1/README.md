# 🚀 FastAPI Dependency Injection Examples

This project demonstrates how to use **Dependency Injection** in FastAPI using various patterns:

- ✅ Simple dependencies
- 🧠 Dependencies with parameters
- 🔐 Authentication-like behavior with query parameters
- 🔁 Multiple dependencies in one route
- 📦 Class-based dependencies with error handling (404)

---

## 🔧 Create a Project In UV With Installation

```bash
uv init fastdca_p1
cd fastdca_p1
uv venv
source .venv/bin/activate
uv add "fastapi[standard]"
```

Or:

```bash
pip install "fastapi[standard]"
```

## ▶️ Run the Server

```bash
uvicorn main:app --reload
```

## 🧪 Endpoints Overview

---

### 1. ✅ Simple Dependency

**URL:**
```http
GET /get_simple_goal
```

**Description:**  
Returns a static goal using a dependency function.

### 2. 🧠 Dependency with Parameters

**URL:**
```http
GET /get_goal?username=Areeba%20Zafar
```

**Description:**  
Returns the same goal with dynamic username passed as a parameter.

### 3. 🔐 Dependency with Query Parameters (Login Example)

**URL:**
```http
GET /signin?username=areeba&password=areeba
```

**Description:**  
Validates login using query parameters. Returns success/failure message.

## 4. 🔁 Multiple Dependencies Example

**URL:**
```http
GET /main/0
```

**Description:**  
Takes `num` as a path parameter and calculates a total using 2 separate dependencies:

- ➕ Adds 1 in first dependency  
- ➕ Adds 2 in second dependency  
- ➕ Then sums everything

## 5. 📦 Class-based Dependency: GetObjOr404

### 📝 Blog API

**URL Examples:**
- ✅ `GET /blog/3` → `"Deep Learning Blog"`
- ❌ `GET /blog/4` → `404 Not Found`

### 👤 User API

**URL Examples:**
- ✅ `GET /user/15` → `"Nabeel"`
- ❌ `GET /user/3` → `404 Not Found`

### 📄 Description
Uses a class as a callable dependency that checks whether the requested object exists.  
If the object is not found, it returns a **404 Not Found** error.

---

### 📁 Data Used

#### Blogs

```python
{
    "1": "Generative AI Blog",
    "2": "Machine Learning Blog",
    "3": "Deep Learning Blog"
}
```

#### Users

```python
{
    "7": "Areeba",
    "15": "Nabeel"
}
```

---

## 💡 Key Concepts

### 🔧 `Depends` helps inject shared logic like:

- 🔐 **Authentication**
- ✅ **Validation**
- 📦 **Data Fetching**

---

### 🧩 Types of Dependencies in FastAPI

- ✅ **Plain functions**
- ✅ **Functions with parameters**
- ✅ **Class with `__call__` method**

---

### ⚙️ FastAPI Behavior

- Automatically **resolves dependencies per request**
- **Caches dependencies** per request (so they aren’t repeatedly called in the same request)

---

### Author

**Made with ❤️ by Areeba Zafar**
