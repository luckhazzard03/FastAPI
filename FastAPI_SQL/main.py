from fastapi import FastAPI, HTTPException

from db import session
from models import Todo
from service import todo_service

app = FastAPI()

@app.post('/')
async def create_todo(text: str, is_complete: bool = False):
    todo = todo_service.create_todo(session, text, is_complete )
    return {"todo added": todo.text}

@app.get("/{id}")
async def get_todo(id: int):
    todo = session.query(Todo).filter(Todo.id == id).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@app.put("/{id}")
async def update_todo(id: int, new_text: str = "", is_complete: bool = False):
    todo = session.query(Todo).filter(Todo.id == id).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    if new_text:
        todo.text = new_text
    todo.is_done = is_complete
    session.add(todo)
    session.commit()
    return {"message": "Todo updated", "todo": todo.text}

@app.delete("/{id}")
async def delete_todo(id: int):
    todo = session.query(Todo).filter(Todo.id == id).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    session.delete(todo)
    session.commit()
    return {"message": "Todo deleted", "todo": todo.text}





"""
docker-compose up -d
uvicorn main:app --reload
"""
    
    
