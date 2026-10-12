from fastapi import APIRouter, HTTPException, status

from models.task import Task, TaskOut

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
)

tasks_db: dict[int, Task] = {}
next_task_id = 1


@router.get("/")
def get_tasks():
    return list(tasks_db.values())


@router.post("/")
def create_task(task: Task):
    global next_task_id

    tasks_db[next_task_id] = task
    created_task = tasks_db[next_task_id]
    next_task_id += 1

    return created_task


@router.get("/{task_id}", response_model=TaskOut)
def get_task(task_id: int):
    task = tasks_db.get(task_id)
    return {"id": task_id, **task.model_dump()}

