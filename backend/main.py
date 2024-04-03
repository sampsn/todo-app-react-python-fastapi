from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models import Todo, ListTodosResponse

app = FastAPI()

origins = ["http://localhost:3000", "localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

TODOS = [Todo(id=1, item="Teach class"), Todo(id=2, item="Taxes!")]


@app.get("/todo")
async def get_todos() -> ListTodosResponse:
    return ListTodosResponse(data=TODOS)


@app.post("/todo")
async def create_todo(new_todo: Todo) -> str:
    TODOS.append(new_todo)
    return "Todo added successfully."


@app.put("/todo/{id}")
async def update_todo(id: int, item: dict) -> str:
    for todo in TODOS:
        if todo.id == id:
            todo.item = item["item"]
    return "Todo updated successfully."


@app.delete("/todo/{id}")
async def delete_todo(id: int) -> str:
    for i, todo in enumerate(TODOS):
        if todo.id == id:
            TODOS.pop(i)
    return "Todo deleted successfully."
