# 🛠 FastAPI Practice Project — All-in-One Request Types

This FastAPI project demonstrates the use of all major request methods and parameter types in FastAPI:

- Path Parameters
- Query Parameters
- Request Body with Pydantic
- Headers
- Cookies
- Form Data
- File Uploads
- Combined Request Models

---

## 🚀 Run the Project

Install dependencies and run:

```bash
pip install fastapi uvicorn pydantic
uvicorn main:app --reload
```

---

## 📌 Endpoints Overview

---

## 🔗 API Endpoints

| Method | Endpoint                               | Description                                 |
|--------|----------------------------------------|---------------------------------------------|
| GET    | /                                      | Get all products                            |
| GET    | /items/{item_id}                       | Get item by ID (Path Parameter)             |
| GET    | /products/product                      | Get product by query parameters             |
| POST   | /products/add                          | Add a product (JSON body - Pydantic model)  |
| GET    | /headers/                              | Get User-Agent header                       |
| GET    | /cookies/                              | Get session cookie                          |
| POST   | /login/                                | Submit login form data                      |
| POST   | /upload/                               | Upload a file                               |
| PUT    | /product/validate/{product_id}         | Validate and update product (Combined data) |

---

### ✅ Root: Get All Products

**GET /**  
Returns the list of all products added.

#### 📦 Example Response:
```json
[
  {
    "product_id": 1,
    "product_name": "Example",
    "price": 100,
    "stock": 10
  }
]
```

### 🔷 Path Parameters

**GET /items/{item_id}**
Get item by its unique path ID.

#### 🧪 Example Request:

```bash
GET /items/5
```

#### 📦 Example Response:

```json
{ "item_id": 5 }
```
### 🔷 Query Parameters

**GET /products/product**
Accepts query parameters with validations.

#### 🧪 Example Request:

```bash
GET /products/product?q=Hairpins&price=100&stock=20
```

#### 🧪 Default Request:

```bash
GET /products/product
```
#### 📦 Example Response:

```json
{
  "q": "Hairpins",
  "price": 100,
  "stock": 20
}
```

### 📦 Request Body (Pydantic Model)

**POST /products/add**
Add a product via a JSON body.

#### 📝 Example JSON Body:

```json
{
  "product_id": 1,
  "product_name": "Hair Pins",
  "price": 250.0,
  "stock": 12
}
```

#### 📦 Example Response:

```json
{
  "message": "Product added successfully",
  "data": {
    "product_id": 1,
    "product_name": "Hair Pins",
    "price": 250.0,
    "stock": 12
  }
}
```

### 🧾 Headers

**GET /headers/**
Send User-Agent header.

#### 🧪 Example Header:

```makefile
User-Agent: Mozilla/5.0
```

#### 📦 Example Response:

```json
{ "user_Agent": "Mozilla/5.0" }
```

### 🍪 Cookies

**GET /cookies/**
Send a cookie named session_id.

#### 🧪 Example Cookie:

```ini
session_id=12345
```

#### 📦 Example Response:

```json
{ "session_id": "12345" }
```

### 📝 Form Data

**POST /login/**
Submit login credentials using a form.

#### 🧪 Example Form Fields:

```ini
username=areeba
password=secret123
```

#### 📦 Example Response:

```json
{
  "username": "areeba",
  "password": "secret123"
}
```

### 📁 File Upload

**POST /upload/**
Upload a file using form-data.

#### 🧪 Example Request:
Use Postman or cURL to send a file.

#### 📦 Example Response:

```json
{
  "filename": "example.txt",
  "content_type": "text/plain",
  "size": 120
}
```

### 🔄 Combined Parameters

**PUT /product/validate/{product_id}**
Combines path, query, and body parameters.

#### 🧪 Example Request:

```bash
curl -X PUT "http://127.0.0.1:8000/product/validate/1?q=UpdateProduct" \
-H "Content-Type: application/json" \
-d '{
  "name": "Hair Pins",
  "description": "Colored pins",
  "price": 250
}'
```

#### 📦 Example Response:

```json
{
  "product_id": 1,
  "q": "UpdateProduct",
  "item": {
    "name": "Hair Pins",
    "description": "Colored pins",
    "price": 250
  }
}
```
---

### 💡 Author
**Areeba Zafar**
This project is for learning and demonstration purposes — practice makes perfect! 💪
