from typing import Optional
from pydantic import BaseModel

from app.models import series


class User(BaseModel):
    id: Optional[int]
    user_name : str 
    firstName : str 
    lastName  : str 
    password  : str     
    class Config:
        orm_mode = True

class MovieSerie(BaseModel):
    id: Optional[int]
    name : str
    director    :str
    averge_score:float
    class Config:
        orm_mode = True

class UserFavorites(BaseModel):
    movies:list [str]
    series:list [str]   
    class Config:
        orm_mode = True
        
class CreatMovieSerie(BaseModel):
    name        :str
    director    :str
    class Config:
        orm_mode = True
        
class UserMoiveScore(BaseModel):
    user_name: str
    moive_name: str
    score: float
    description:str
    
    class Config:
        orm_mode = True

class Score(BaseModel):
    user_name: str
    moive_serie_name: str
    score: float
    description:str
    
  
        
class UserSerieScore(BaseModel):
    user_name: str
    serie_name: str
    score: float
    description:str
    
    class Config:
        orm_mode = True
        
class UserMovieFavorite(BaseModel):
    user_name: str
    movie_name: str 
          
    class Config:
        orm_mode = True     
        
class UserSerieFavorite(BaseModel):
    user_name: str
    serie_name: str 
          
    class Config:
        orm_mode = True        

        
class Respuesta(BaseModel):
    msj:str
    error: str
    
class Username(BaseModel):
    username:str
    password:str

    
   


   