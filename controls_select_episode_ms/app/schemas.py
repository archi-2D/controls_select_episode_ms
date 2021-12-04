from typing import Optional
from pydantic import BaseModel



        
class UserMoiveScore(BaseModel):
    user_name: str
    moive_name: str
    score: float
    description:str
    
    class Config:
        orm_mode = True
        
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

    
   


   