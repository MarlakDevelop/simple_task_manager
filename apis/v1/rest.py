from typing import Optional, List
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Form, HTTPException, status
import apps.task.services as task_services
from apis.v1 import schemas


tasks_router = APIRouter(prefix='/api/v1/tasks', tags=["tasks"])


@tasks_router.get('/', response_model=List[schemas.Task], status_code=status.HTTP_200_OK)
async def get_list():  # List
    result = await task_services.read_tasks()
    return result


@tasks_router.get('/{tid:int}', response_model=schemas.Task, status_code=status.HTTP_200_OK)
async def get_single(tid: int):  # Single item
    checker = await task_services.check_task_id_for_existing(tid)
    if not checker:
        raise HTTPException(status_code=404, detail="Task not found")
    result = await task_services.read_task(tid)
    return result


@tasks_router.post('/', response_model=schemas.Task, status_code=status.HTTP_201_CREATED)
async def post(
    task: schemas.TaskPost
):  # Single item
    completed = task.completed if task.completed is not None else False
    result = await task_services.create_task(name=task.name, completed=completed)
    return result


@tasks_router.put('/{tid:int}', response_model=schemas.Task, status_code=status.HTTP_202_ACCEPTED)
async def put(
    tid: int,
    task: schemas.TaskPut
):  # Single item
    checker = await task_services.check_task_id_for_existing(tid)
    if not checker:
        raise HTTPException(status_code=404, detail="Task not found")
    update_data = task.dict(exclude_unset=False)
    result = await task_services.update_task(
        tid=tid,
        **update_data
    )
    return result


@tasks_router.patch('/{tid:int}', response_model=schemas.Task, status_code=status.HTTP_202_ACCEPTED)
async def patch(
    tid: int,
    task: schemas.TaskPatch
):  # Single item
    checker = await task_services.check_task_id_for_existing(tid)
    if not checker:
        raise HTTPException(status_code=404, detail="Task not found")
    update_data = task.dict(exclude_unset=True)
    result = await task_services.update_task_partial(tid=tid, **update_data)
    return result


@tasks_router.delete('/{tid:int}', status_code=status.HTTP_202_ACCEPTED)
async def delete(tid: int):  # Single item
    checker = await task_services.check_task_id_for_existing(tid)
    if not checker:
        raise HTTPException(status_code=404, detail="Task not found")
    await task_services.destroy_task(tid=tid)
