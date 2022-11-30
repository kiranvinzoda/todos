from typing import List
from fastapi import Depends, FastAPI, HTTPException, Request, Response
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import User, Todo
from fastapi.middleware.cors import CORSMiddleware
import schemas
import models
import crud

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/add_todo/", response_model=schemas.Show_Todo)
def create_todo(todo: schemas.Crate_Todo, db: Session = Depends(get_db)):
    return crud.create_todo(db=db, todo=todo)



@app.get("/show_todos/", response_model=List[schemas.Show_Todo])
def read_users(db: Session = Depends(get_db)):
    todos = crud.get_all_todos(db)
    return todos


@app.get("/get_todo/{todo_id}", response_model=schemas.Show_Todo)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = crud.get_todo(db, todo_id=todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo


@app.put("/update_todo/{todo_id}", response_model=schemas.Show_Todo)
def put_todo(todo_id: int, todo: schemas.Crate_Todo, db: Session = Depends(get_db)):
    db_todo = crud.get_todo(db, todo_id=todo_id)

    if db_todo is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_todo = crud.update_todo(db, todo_id=todo_id, todo = todo)    
    return db_todo


@app.delete("/delete_todo/{todo_id}")
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = crud.get_todo(db, todo_id=todo_id)
    print(db_todo)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    db_todo = crud.delete_todo(db, todo_id=todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="User not found")
   


# @app.get("/users/", response_model=List[schemas.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = crud.get_users(db, skip=skip, limit=limit)
#     return users


# @app.get("/users/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user

