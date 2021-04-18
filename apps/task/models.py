import ormar
from core.database import BaseMeta


class Task(ormar.Model):
    class Meta(BaseMeta):
        tablename = "tasks"
        orders_by = ["-id"]

    id: int = ormar.Integer(primary_key=True, unique=True)
    name: str = ormar.String(max_length=100)
    completed: bool = ormar.Boolean(default=False)
