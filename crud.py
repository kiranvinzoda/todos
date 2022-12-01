from sqlalchemy.orm import Session

import models
import schemas


def get_todo(db: Session, todo_id: int):
    return db.query(models.Todo).filter(models.Todo.id == todo_id , models.Todo.is_active == True).first()


def get_todo_by_id(db: Session, id: int):
    return db.query(models.Todo).filter(models.Todo.id == id, models.Todo.is_active == True).first()


def get_all_todos(db: Session):
    return db.query(models.Todo).filter(models.Todo.is_active == True).all()


def create_todo(db: Session, todo: schemas.Create_Todo):
    
    db_todo = models.Todo(title=todo.title, desc=todo.desc)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def update_todo(db: Session, todo_id: int, todo: schemas.Create_Todo):
    print(todo_id)
    print(todo) 
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id, models.Todo.is_active == True).first()
    db_todo.title = todo.title
    db_todo.desc = todo.desc
    db.commit()
    return db_todo

def delete_todo(db: Session, todo_id: int):
    
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id, models.Todo.is_active == True).first()
    db_todo.is_active = False
    db_todo = db.commit()
    return True

