from sqlalchemy.orm import Session

import models
import schemas


def get_todo(db: Session, todo_id: int):
    return db.query(models.Todo).filter(models.Todo.id == todo_id).first()


def get_todo_by_id(db: Session, id: int):
    return db.query(models.Todo).filter(models.Todo.id == id).first()


def get_all_todos(db: Session):
    return db.query(models.Todo).all()


def create_todo(db: Session, todo: schemas.Crate_Todo):
    
    db_todo = models.Todo(title=todo.title, desc=todo.desc)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def update_todo(db: Session, todo_id: int, todo: schemas.Crate_Todo):
    db_todo = db.query(models.Todo).filter(models.Todo.id == id).update(vars(todo))
    db.commit()
    return db_todo



def delete_todo(db: Session, todo_id: int):
    
    db_todo = db.query(models.Todo).filter(models.Todo.id == id).first()
    print(db_todo)
    db_todo.is_active = False
    db.commit()
    return db_todo

