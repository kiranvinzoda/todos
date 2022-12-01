from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base



class User(Base):
    __tablename__ = "users"

    id = Column(String(36), primary_key=True)
    name = Column(String(50))
    email = Column(String(50))
    password = Column(String(255))
    is_active = Column(Boolean, default=True)
 

    # todo = relationship("Todo", backref="owner")



class Todo(Base):
    __tablename__ = "todo"

    id = Column(String(36), primary_key=True)
    title = Column(String(50))
    desc = Column(String(50))
    # owner = Column(Integer, ForeignKey("users.id"), default=1)
    is_active = Column(Boolean, default=True)

    # owner = relationship("User", backref="todo")


