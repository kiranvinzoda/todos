from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(50), unique=True , index=True)
    password = Column(String(50))
    is_active = Column(Boolean, default=True)
 

    # todo = relationship("Todo", backref="owner")



class Todo(Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), unique=True, index=True)
    desc = Column(String(50))
    # owner = Column(Integer, ForeignKey("users.id"), default=1)
    is_active = Column(Boolean, default=True)

    # owner = relationship("User", backref="todo")


