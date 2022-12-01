from sqlalchemy.orm import Session

import models
import schemas
import uuid
from auth import AuthHandler
auth_handler = AuthHandler()



def generate_id():
    id = str(uuid.uuid4())
    return id


def user_varification(db: Session, token : str):
    result_email = auth_handler.decode_token(token)
    user_record = db.query(models.User).filter(models.User.email == result_email).first()
    if user_record is not None:
        return True
    else:
        return False


def get_todo(db: Session, todo_id: str):
    return db.query(models.Todo).filter(models.Todo.id == todo_id , models.Todo.is_active == True).first()


def get_todo_by_id(db: Session, id: str):
    return db.query(models.Todo).filter(models.Todo.id == id, models.Todo.is_active == True).first()


def get_all_todos(db: Session):
    return db.query(models.Todo).filter(models.Todo.is_active == True).all()


def create_todo(db: Session, todo: schemas.Create_Todo):
    
    todo_id = generate_id()
    db_todo = models.Todo(id = todo_id,title=todo.title, desc=todo.desc)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def update_todo(db: Session, todo_id: str, todo: schemas.Create_Todo):

    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id, models.Todo.is_active == True).first()
    db_todo.title = todo.title
    db_todo.desc = todo.desc
    db.commit()
    return db_todo

def delete_todo(db: Session, todo_id: str):
    
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id, models.Todo.is_active == True).first()
    db_todo.is_active = False
    db_todo = db.commit()
    return True

def create_user(db: Session, user: schemas.Create_Usr ,password: str):
    
    user_id = generate_id()
    db_user = models.User(id = user_id,name=user.name, email=user.email,password=password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_all_users(db: Session):
    return db.query(models.User).filter(models.User.is_active == True).all()

def get_user(db: Session, user_id: str):
    return db.query(models.User).filter(models.User.id == user_id , models.User.is_active == True).first()

def get_user_by_email(db: Session, user_email : str):
    return db.query(models.User).filter(models.User.email == user_email , models.User.is_active == True).first()















