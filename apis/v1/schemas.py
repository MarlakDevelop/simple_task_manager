from typing import Optional
from pydantic import BaseModel, constr


class Task(BaseModel):
    id: int
    name: constr(max_length=100)
    completed: bool


class TaskPost(BaseModel):
    name: constr(max_length=100)
    completed: Optional[bool]


class TaskPut(BaseModel):
    name: constr(max_length=100)
    completed: bool


class TaskPatch(BaseModel):
    name: Optional[constr(max_length=100)]
    completed: Optional[bool]