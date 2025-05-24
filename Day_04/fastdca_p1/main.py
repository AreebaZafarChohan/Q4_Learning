from contextlib import asynccontextmanager
from fastapi import Cookie, FastAPI, File, Form, Header, Path, Query , Body, UploadFile
from pydantic import BaseModel

# Use lifespan for startup setup
@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.products = []  # initialize once at startup
    yield

app = FastAPI(lifespan=lifespan)


# Path() Parameter

@app.get("/items/{item_id}")
async def read_item(
    item_id: int = Path(
        ..., # ... means it is required 
        title="Item Id",
        description="Unique ID for each item",
        ge=1, # greater than or equal to 1
    )
):
    return {"item_id": item_id}

# Query() Parameter

@app.get("/products/product")
async def read_product(
    q: str | None = Query(
        "Default Product you can change it..." ,
        title="Query Param",
        description="This is a query parameter for product",
        min_length=3,
        max_length=60
    ),
    price: int = Query(50, ge=0),    
    stock: int = Query(10, le=200)
):
    return {"q": q, "price": price, "stock": stock }


# Request Body -> Body() with pydantic model

class Product(BaseModel):
    product_id: int
    product_name: str
    price: float
    stock: int

    
@app.post("/products/add")
async def add_product(product: Product = Body(..., description="Product details to add")):
    app.state.products.append(product)
    return {
        "message": "Product added successfully",
        "data": product
    }
        

# Root of API which shows products list       

@app.get("/")
async def read_root():
    return app.state.products


# Headers

@app.get("/headers/")
async def read_headers(user_agent: str = Header(...,)):
    return {"user_Agent": user_agent}

# Cookies

@app.get("/cookies/")
async def read_cookies(session_id: str = Cookie(715)):
    return {"session_id": session_id}


# Form

@app.post("/login/")
async def login(username: str = Form(...,), password: str = Form(...,)):
    return {"username": username , "password": password}


# File Upload
@app.post("/upload/")
async def upload_file(file: UploadFile = File(...,)):
    content = await file.read()
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size": len(content)
    } 

# Combine params

class Item(BaseModel):
    name: str
    description: str
    price: int
    
@app.put("/product/validate/{product_id}")
async def update_product(
    product_id: int = Path(..., title="Product Id", ge=1),
    q: str = Query("This is a default query you can replace it.", min_length=3),
    item: Item = Body(
        {
            "name": "Hair Pins",
            "description": "This is the packet of hair pins in different colors. It has 12 pins in each packet",
            "price": 250
        },
        description="Optional product data (JSON body)")
):
    result: dict[str, object] = { "product_id": product_id }
    if q:
        result.update({"q": q})
    if item:
        result.update({"item": item})  # type: ignore
    return result  