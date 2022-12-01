from pydantic import BaseModel



class Show_User(BaseModel):
    id: int
    email : str
    password : str
    is_active : bool

    class Config:
        orm_mode = True


class Show_Todo(BaseModel):
    id: int
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





