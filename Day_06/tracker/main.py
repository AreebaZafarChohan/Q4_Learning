from fastapi import FastAPI, HTTPException
from schemas import UserCreate, User, TaskCreate, Task, TaskUpdate
import curd

app: FastAPI = FastAPI()

@app.post("/users/", response_model=User)
def create_user(user: UserCreate):
    return curd.create_user(user)

@app.get("/user/{user_id}", response_model=User)
def read_user(user_id: int):
    user = curd.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    user = curd.delete_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"mesage": "User Deleted"}

@app.post("/tasks/", response_model=Task)
def create_task(task: TaskCreate):
    if not curd.get_user(task.user_id):
        raise HTTPException(status_code=404, detail="User not found")
    return curd.create_task(task)

@app.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: int):
    task = curd.get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_update: TaskUpdate):
    task = curd.update_task(task_id, update_task)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    task = curd.delete_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted"}

@app.get("/users/{user_id}/tasks", response_model=list[Task])
def get_tasks_for_user(user_id: int):
    return curd.get_tasks_by_user(user_id)

