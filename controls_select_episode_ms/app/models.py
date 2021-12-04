from decimal import Decimal
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from .conexion import Base

user_id = 'user.id'
series_id = 'series.id'

class chapter(Base):
    __tablename__ = "chapter"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(50))
    director = Column(String(50))
    duration = Column(Integer)
    averge_score = Column(Float)
    season_id = Column(Integer, ForeignKey('season.id'))
        
class season(Base):
    __tablename__ = "season"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(50))
    chapters = relationship("chapter")
    series_id = Column(Integer, ForeignKey(series_id))
    
class series(Base):
    __tablename__ = "series"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(50),nullable=False, unique=True)
    director = Column(String(50))
    averge_score = Column(Float)
    seasons = relationship("season")
    user_series_score = relationship("user_series_score")
    user_series_favorites=relationship("user_series_favorites")
    
class user(Base):
    __tablename__ = "user"
    id = Column(Integer,primary_key=True,index=True)
    user_name = Column(String(50),nullable=False, unique=True)
    fristName = Column(String(50))
    lastName = Column(String(50))
    password = Column(String(50))
    user_series_score = relationship("user_series_score")
    user_series_favorites=relationship("user_series_favorites")
    user_movies_score = relationship("user_movies_score")
    user_movies_favorites=relationship("user_movies_favorites")
    
class user_series_score(Base):
    __tablename__ = "user_series_score"
    id = Column(Integer,primary_key=True,index=True)
    user_id = Column(Integer, ForeignKey(user_id))
    series_id = Column(Integer, ForeignKey(series_id))
    score = Column(Float)
    description = Column(String(100))

class user_series_favorites(Base):
    __tablename__ = "user_series_favorites"
    id = Column(Integer,primary_key=True,index=True)
    user_id = Column(Integer, ForeignKey(user_id))
    series_id = Column(Integer, ForeignKey(series_id))
       
class movies(Base):
    __tablename__ = "movies"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(50),nullable=False, unique=True)
    director = Column(String(50))
    averge_score = Column(Float)    
    user_movies_score = relationship("user_movies_score")
    user_movies_favorites=relationship("user_movies_favorites")
    
class user_movies_score(Base):
    __tablename__ = "user_movies_score"
    id = Column(Integer,primary_key=True,index=True)
    user_id = Column(Integer, ForeignKey(user_id))
    movies_id = Column(Integer, ForeignKey('movies.id'))
    score = Column(Float)
    description = Column(String(100))

class user_movies_favorites(Base):
    __tablename__ = "user_movies_favorites"
    id = Column(Integer,primary_key=True,index=True)
    user_id = Column(Integer, ForeignKey(user_id))
    movies_id = Column(Integer, ForeignKey('movies.id'))
       
