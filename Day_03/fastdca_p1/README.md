# DACA Chatbot API with Pydantic Examples

A FastAPI-based chatbot API developed by Areeba Zafar, showcasing Pydantic data validation in Python.

## Features

- **FastAPI Implementation**:
  - RESTful endpoints for chatbot functionality
  - Automatic API documentation
  - Request validation
  - Error handling

- **Pydantic Examples**:
  - Basic model validation
  - Nested models
  - Custom validators
  - Email validation
  - Error handling patterns


## Project Structure
  - **main.py # FastAPI application with chatbot endpoints**
  - **pydantic_example_1.py # Basic Pydantic model usage**
  - **pydantic_example_2.py # Nested models with email validation**
  - **pydantic_example_3.py # Custom field validators**

## API Endpoints (main.py)

### Base URL
- `GET /` - Welcome message and API documentation link

### User Management
- `GET /users/{user_id}` - Get user information with optional role parameter

### Chat Functionality
- `POST /chat/` - Process chat messages with validation

## Pydantic Examples

### 1. Basic Model (pydantic_example_1.py)
```python
class User(BaseModel):
    id: int
    name: str
    email: str
    age: int | None = None  # Optional field
```

## 2. Nested Models with Email Validation (pydantic_example_2.py)

```python
from pprint import pprint
from pydantic import BaseModel, EmailStr

class Address(BaseModel):
    street: str
    city: str
    zip_code: str
    
class UserWithAddress(BaseModel):
    id: int
    name: str
    email: EmailStr  # Built-in validator for email format
    addresses: list[Address]  # List of nested Address models
```

## 3. Custom Validators (pydantic_example_3.py)

```python
from pydantic import BaseModel, EmailStr, field_validator, ValidationError

class UserWithAddress(BaseModel):
    id: int
    name: str
    email: EmailStr
    addresses: list[Address]
    
    @field_validator("name")
    def name_validation(cls, value):
        if not value.strip():
            raise ValueError("Name cannot be empty")
        if len(value) < 2:
            raise ValueError("Name must be at least 2 characters long")
        if not value[0].isupper():
            raise ValueError("Name must start with capital letter")
        return value

```

### Install dependencies:
```bash
pip install fastapi uvicorn pydantic[email]
```

## Usage Examples

### API Request
```python
import requests

response = requests.post(
    "http://localhost:8000/chat/",
    json={
        "user_id": "test123",
        "text": "Hello chatbot",
        "metadata": {}
    }
)
```

### Pydantic Validation

```python
try:
    user = User(id="invalid", name="Areeba", email="test@example.com")
except ValidationError as e:
    print(f"Error: {e}")
```

## Blog Post
For a detailed walkthrough of this implementation, read our blog post:  
[Building Robust APIs with FastAPI and Pydantic Validation](https://medium.com/@areebazafar715/building-a-chat-application-in-fastapi-with-pydantic-ba5ba166832f)  

## Key Concepts Demonstrated
- ✔️ Data validation with Pydantic  
- ✔️ Nested model structures  
- ✔️ Custom validation logic  
- ✔️ Error handling patterns  
- ✔️ FastAPI integration  

## Requirements
- Python 3.10+  
- FastAPI  
- Pydantic v2  
- Uvicorn  

Made with ❤ by **Areeba Zafar**
