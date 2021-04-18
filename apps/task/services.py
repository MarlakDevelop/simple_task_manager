from typing import List, Optional
from .models import Task


async def check_task_id_for_existing(tid: int) -> bool:
    task = await Task.objects.get_or_none(id=tid)
    if task:
        return True
    return False


async def create_task(name: str, completed: bool = False) -> Task:
    task = Task(name=name, completed=completed)
    await task.save()
    return task


async def read_tasks() -> List[Optional[Task]]:
    tasks = await Task.objects.all()
    return tasks


async def read_task(tid: int) -> Task:
    task = await Task.objects.get(id=tid)
    return task


async def update_task(tid: int, name: str, completed: bool) -> Task:
    task = await Task.objects.get(id=tid)
    kwargs = {
        'name': name,
        'completed': completed
    }
    task.update(**kwargs)
    task.save()
    return task


async def update_task_partial(tid: int, name: str or None = None, completed: bool or None = None) -> Task:
    task = await Task.objects.get(id=tid)
    kwargs = {}
    if name is not None:
        kwargs['name'] = name
    if completed is not None:
        kwargs['completed'] = completed
    task.update(**kwargs)
    task.save()
    return task


async def destroy_task(tid: int) -> bool:
    task = await Task.objects.get(id=tid)
    await task.delete()
    return True
