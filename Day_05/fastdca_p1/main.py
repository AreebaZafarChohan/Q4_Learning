from fastapi import Depends, FastAPI, HTTPException, status, Query, Path
from typing import Annotated


app: FastAPI = FastAPI()

# 1. Hello Dependency 
# http://127.0.0.1:8000/get_simple_goal

def get_simple_goal():
    return {"goal": "We are building AI Agents Workforce"}

@app.get("/get_simple_goal")
def simple_goal(response: Annotated[dict, Depends(get_simple_goal)]):
      return response


# 2. Dependency with parameters
# http://127.0.0.1:8000/get_goal?username=Areeba%20Zafar
# OR http://127.0.0.1:8000/get_goal

def get_goal(username: str):
    return {"goal":  "We are building AI Agents Workforce", "username": username}

@app.get("/get_goal")
def get_my_goal(response: Annotated[dict, Depends(get_goal)]):
    return response

# 3. Dependency with Query parameters
# http://127.0.0.1:8000/signin?username=areeba&password=areeba
# OR http://127.0.0.1:8000/signin

def dep_login(username: str = Query(None), password: str = Query(None)):
    if username == "areeba" and password == "areeba":
        return {"message": "Login Successful"}
    else:
        return {"message": "Login Failed"}
    
@app.get("/signin")
def sign_in(user: Annotated[dict, Depends(dep_login)]):
    return user    

# 4. Multiple Dependencies
# http://127.0.0.1:8000/main/0
# OR http://127.0.0.1:8000/main

def dependency_func1(num: int):
    num = int(num)
    num += 1
    return num

def dependency_func2(num: int):
    num = int(num)
    num += 2
    return num

@app.get("/main/{num}")
def get_main(num: int, num1: Annotated[int, Depends(dependency_func1)], num2: Annotated[int, Depends(dependency_func2)]):
    total = num + num1 + num2
    return f"Total numbers are {total}"


# 5. Classes

blogs = {
     "1": "Generative AI Blog",
    "2": "Machine Learning Blog",
    "3": "Deep Learning Blog"
}

users = {
    "7": "Areeba",
    "15": "Nabeel"
}

class GetObjOr404():
    def __init__(self, model) -> None:
        self.model = model
        
    def __call__(self, id: str) -> None:
        obj = self.model.get(id)
        if not obj:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Object ID {id} not found")
        return obj
    
blog_dependency = GetObjOr404(blogs)

# http://127.0.0.1:8000/blog/4 -> {"detail":"Object ID 4 not found"}

# OR http://127.0.0.1:8000/blog/3 -> "Deep Learning Blog"

# OR http://127.0.0.1:8000/blog


@app.get("/blog/{id}")
def get_blog(blog_name: Annotated[str, Depends(blog_dependency)]):
    return blog_name        

user_dependency = GetObjOr404(users)

# http://127.0.0.1:8000/user

# OR http://127.0.0.1:8000/user/3 -> {"detail":"Object ID 3 not found"}

# OR http://127.0.0.1:8000/user/15 -> "Nabeel"


@app.get("/user/{id}")
def get_user(user_name: Annotated[str, Depends(user_dependency)]):
    return user_name