from db import Session
from models.todo import Todo


def create_todo( session:Session, is_complete: bool = False):
    todo = Todo(text=text, is_done=is_complete)
    session.add(todo)
    session.commit()
    return todo