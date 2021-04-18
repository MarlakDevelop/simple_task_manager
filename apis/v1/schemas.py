from pydantic import BaseModel, constr


class Task(BaseModel):
    id: int
    name: constr(max_length=100)
    completed: bool
