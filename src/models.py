import os
import sys
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    first_name = Column(String(250))
    last_name = Column(String(250))
    email = Column(String(250), nullable=False)
    follower = relationship("Follower", backref="user")
    post = relationship("Post", backref='user')
    comment_relation = relationship("Comment", backref="author")
    


class Follower(Base):
    __tablename__ = 'follower'
    id_follow = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user_to_id = Column(Integer, ForeignKey('user.id'), nullable=False)


class Post(Base):
    __tablename__='post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    comment_relationship = relationship('comment', backref="post")
    media_relationship = relationship('media', backref='post')

class Comment(Base):
    __tablename__='comment'
    id = Column(Integer, primary_key=True)
    comment_text =Column(String(250), nullable=False)
    author_id = Column(Integer, ForeignKey('author.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)


class Media(Base):
    __tablename__='media'
    id = Column(Integer, primary_key=True)
    url = Column(String(250), nullable=False)
    type = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    



render_er(Base, 'diagram.png')