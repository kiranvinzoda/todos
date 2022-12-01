from pydantic import BaseModel


class Show_User(BaseModel):
    id: str
    email : str
    password : str
    is_active : bool

    class Config:
        orm_mode = True


class Show_Todo(BaseModel):
    id: str
    title : str
    desc : str
    is_active : bool

    class Config:
        orm_mode = True



class Create_Todo(BaseModel):
    
    title : str
    desc : str


    class Config:
        orm_mode = True


class Create_Usr(BaseModel):
    
    name : str
    email : str
    password : str


    class Config:
        orm_mode = True


class Show_User(BaseModel):
    id: str
    name : str
    email : str
    password : str
    is_active : bool

    class Config:
        orm_mode = True


class AuthDetails(BaseModel):
    email: str
    password: str