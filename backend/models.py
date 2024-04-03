from pydantic import BaseModel


class Todo(BaseModel):
    id: int
    item: str


class ListTodosResponse(BaseModel):
    data: list[Todo]
