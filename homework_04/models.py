"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

from sqlalchemy import (
    Column,
    String,
    Text,
    Integer,
    ForeignKey
)
from sqlalchemy .orm import relationship
from base import Base


class User(Base):
    def __init__(self, name, username, email):
        self.name = name
        self.username = username
        self.email = email

    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.name, self.username, self.email)

    name = Column(String)
    username = Column(String, unique=True)
    email = Column(String, unique=True)

    posts = relationship("Post", back_populates="user")


class Post(Base):
    def __init__(self, user_id, title, body):
        self.user_id = user_id
        self.title = title
        self.body = body

    def __repr__(self):
        return "<Post('%s','%s', '%s')>" % (self.user_id, self.title, self.body)

    title = Column(String)
    body = Column(Text)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    user = relationship("User", back_populates="posts")
