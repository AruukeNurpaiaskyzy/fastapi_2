# from fastapi import FastAPI
# app = FastAPI()
# @app.get('/')
# async def root():
#     return {'message': 'Hello FastAPI'}

from pydantic import BaseModel
from typing import List

class Task(BaseModel):
    id: int
    title: str
    completed: bool = False
    task_db = []
@app.post("/tasks/", response_model=Task)
def create_task(task: Task):
    task_db.append(task)
    return task
@app.get("/tasks/", response_model=List[Task])
def get_tasks():
    return tasks_db р