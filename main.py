from typing import List
from fastapi import Depends, FastAPI, HTTPException, Request, Response, Header
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import User, Todo
from fastapi.middleware.cors import CORSMiddleware
import schemas
import models
import crud
from auth import AuthHandler


models.Base.metadata.create_all(bind=engine)
app = FastAPI()
auth_handler = AuthHandler()

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


@app.post("/add_todo/", tags=["todo"], response_model=schemas.Show_Todo)
def create_todo(todo: schemas.Create_Todo, db: Session = Depends(get_db), token: str = Header(None)):
    check = crud.user_varification(db, token= token )
    if check:
        return crud.create_todo(db=db, todo=todo, token= token)
    else:
        raise HTTPException(status_code=404, detail="Token not valid")   


@app.get("/show_todos/", tags=["todo"], response_model=List[schemas.Show_Todo])
def read_todos(db: Session = Depends(get_db), offset: int = 0, limit: int = 100, token: str = Header(None)):
    check = crud.user_varification(db, token= token )
    if check:
        return crud.get_all_todos(db, token= token, limit = limit, offset = offset )
    else:
        raise HTTPException(status_code=404, detail="Token not valid")          


@app.get("/get_todo/{todo_id}", tags=["todo"], response_model=schemas.Show_Todo)
def read_todo(todo_id: str, db: Session = Depends(get_db), token: str = Header(None)):
    check = crud.user_varification(db, token= token )
    if check:
        db_todo = crud.get_todo(db, todo_id=todo_id, token= token)
        if db_todo is None:
            raise HTTPException(status_code=404, detail="Todo not found")
        return db_todo
    else:
        raise HTTPException(status_code=404, detail="Token not valid") 
        
    

@app.put("/update_todo/{todo_id}", tags=["todo"], response_model=schemas.Show_Todo)
def put_todo(todo_id: str, todo: schemas.Create_Todo, db: Session = Depends(get_db), token: str = Header(None)):
    check = crud.user_varification(db, token= token )
    if check:
        db_todo = crud.get_todo(db, todo_id=todo_id, token= token)
        if db_todo is None:
            raise HTTPException(status_code=404, detail="User not found")
        update_tod = crud.update_todo(db, todo_id=todo_id, todo = todo)    
        return update_tod      
    else:
        raise HTTPException(status_code=404, detail="Token not valid") 


@app.delete("/delete_todo/{todo_id}", tags=["todo"])
def read_todo(todo_id: str, db: Session = Depends(get_db), token : str = Header(None)):
    check = crud.user_varification(db, token= token )
    if check:
        db_todo = crud.get_todo(db, todo_id=todo_id, token= token)
        if db_todo is None:
            raise HTTPException(status_code=404, detail="Todo not found")
        db_todo = crud.delete_todo(db, todo_id=todo_id)
        if db_todo:
            raise HTTPException(status_code=404, detail="Todo deleted succesfully")
    else:
        raise HTTPException(status_code=404, detail="Token not valid")  



@app.get("/search_todo_by_key/{search_key}", tags=["todo"], response_model=List[schemas.Show_Todo])
def search_todo_by_key(search_key: str, db: Session = Depends(get_db), token: str = Header(None)):
    check = crud.user_varification(db, token= token )
    if check:
        db_todo = crud.get_todo_by_search_key(db, search_key=search_key)
        if db_todo is None:
            raise HTTPException(status_code=404, detail="Todo not found")
        return db_todo
    else:
        raise HTTPException(status_code=404, detail="Token not valid") 


@app.get("/show_users/", tags=["user"], response_model=List[schemas.Show_User])
def read_users(db: Session = Depends(get_db)):
    users = crud.get_all_users(db)
    return users


#jwt tokan

@app.post('/user_register', tags=["user"], status_code=201)
def register(user: schemas.Create_Usr , db: Session = Depends(get_db)):
    user_record = crud.get_user_by_email(db=db, user_email=user.email)
    if  user_record is not None :
        raise HTTPException(status_code=400, detail='email is taken')
    hashed_password = auth_handler.get_password_hash(user.password)
    return crud.create_user(db=db, user=user, password = hashed_password)



@app.post('/user_login', tags=["user"])
def login(auth_details: schemas.AuthDetails, db: Session = Depends(get_db)):
    user = None
    user_record = crud.get_user_by_email(db=db, user_email=auth_details.email)
    if user_record is None:
        raise HTTPException(status_code=401, detail='invalid email')
         
    if (user_record is None) or (not auth_handler.verify_password(auth_details.password, user_record.password)):
        raise HTTPException(status_code=401, detail='Invalid username and/or password')
    token = auth_handler.encode_token(user_record.id)
    return { "user": user_record, 'token': token }




# image upload













