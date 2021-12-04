from os import name
from typing import List
from fastapi import FastAPI
from fastapi.param_functions import Depends
from pydantic.types import Json
from sqlalchemy.orm.session import Session
from starlette.responses import RedirectResponse
from . import models,schemas
from .conexion import SessionLocal,engine

models.Base.metadata.create_all(bind =engine)

app = FastAPI()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
        
        
@app.get("/")
def main():
    return RedirectResponse(url="/docs/")





@app.post('/usuarios/movie_score',response_model=schemas.Respuesta)
def user_movie_score(entrada:schemas.UserMoiveScore, db:Session=Depends(get_db)):
    user = db.query(models.user).filter_by(user_name=entrada.user_name).first()
    moive = db.query(models.movies).filter_by(name=entrada.moive_name).first()
    moive_score = db.query(models.user_movies_score).filter_by(movies_id=moive.id).all()
    averge_score = 0.0
    for movies in moive_score:
        averge_score += movies.score        
    averge_score+=entrada.score    
    if len(moive_score) > 0:
        averge_score= averge_score/(len(moive_score)+1)   
    user_moive_score =  models.user_movies_score(user_id = user.id, movies_id = moive.id, score = entrada.score,description = entrada.description )
    moive.averge_score = averge_score
    db.add(user_moive_score)
    db.commit()
    db.refresh(user_moive_score)
    db.refresh(moive)
    respuesta = schemas.Respuesta(msj="funciona")
    return respuesta

@app.post('/usuarios/series_score',response_model=schemas.Respuesta)
def user_series_score(entrada:schemas.UserSerieScore, db:Session=Depends(get_db)):
    user = db.query(models.user).filter_by(user_name=entrada.user_name).first()
    serie = db.query(models.series).filter_by(name=entrada.serie_name).first()
    serie_score = db.query(models.user_series_score).filter_by(series_id=serie.id).all()  
    averge_score = 0.0
    for series in serie_score:
        averge_score += series.score        
    averge_score+=entrada.score    
    if len(serie_score) > 0:
        averge_score= averge_score/(len(serie_score)+1)         
    user_serie_score =  models.user_series_score(user_id = user.id, series_id = serie.id,  score = entrada.score,description = entrada.description )
    serie.averge_score = averge_score
    db.add(user_serie_score)
    db.commit()
    db.refresh(user_serie_score)
    db.refresh(serie)
    respuesta = schemas.Respuesta(msj="funciona")
    return respuesta

@app.post('/usuarios/movies_favorite',response_model=schemas.Respuesta)
def user_movies_favorites(entrada:schemas.UserMovieFavorite, db:Session=Depends(get_db)):
    user = db.query(models.user).filter_by(user_name=entrada.user_name).first()
    movie = db.query(models.movies).filter_by(name=entrada.movie_name).first()
    user_movies_favorites =  models.user_movies_favorites(user_id = user.id, movies_id = movie.id)
    db.add(user_movies_favorites)
    db.commit()
    db.refresh(user_movies_favorites)
    respuesta = schemas.Respuesta(msj="funciona")
    return respuesta

@app.post('/usuarios/series_favorite',response_model=schemas.Respuesta)
def user_series_favorites(entrada:schemas.UserSerieFavorite, db:Session=Depends(get_db)):
    user = db.query(models.user).filter_by(user_name=entrada.user_name).first()
    serie = db.query(models.series).filter_by(name=entrada.serie_name).first()
    user_series_favorites =  models.user_series_favorites(user_id = user.id, series_id = serie.id)
    db.add(user_series_favorites)
    db.commit()
    db.refresh(user_series_favorites)
    respuesta = schemas.Respuesta(msj="funciona")
    return respuesta


