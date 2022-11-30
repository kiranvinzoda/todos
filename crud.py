from sqlalchemy.orm import Session

import models
import schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_todo_by_id(db: Session, id: int):
    return db.query(models.Todo).filter(models.Todo.id == id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_todo(db: Session, todo: schemas.Crate_Todo):
    
    db_todo = models.Todo(title=todo.title, desc=todo.desc)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo



