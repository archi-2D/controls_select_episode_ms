from ast import If
from os import name
from typing import List, Type
from fastapi import FastAPI
from fastapi.param_functions import Depends
from pydantic.types import Json
from sqlalchemy.orm.session import Session
from starlette.responses import RedirectResponse
from . import models,schemas
from .conexion import SessionLocal,engine
from uuid import uuid4

models.Base.metadata.create_all(bind =engine)

app = FastAPI()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
        
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8443)      
@app.get("/")
def main():
    return RedirectResponse(url="/docs/")

@app.get('/users',response_model= List[schemas.User])
def get_user(db:Session=Depends(get_db)):
    users_db = db.query(models.user).all()    
    return users_db

@app.post('/users/veryUser',response_model= schemas.Respuesta)
def get_user(entrada:schemas.Username, db:Session=Depends(get_db)):

    user_db = db.query(models.user).filter_by(user_name=entrada.username).first()
    if user_db.password == entrada.password :
        return schemas.Respuesta(msj= str(uuid4()), error = "No Error");
    else:
        return schemas.Respuesta(msj="", error = "Invalid credential")
       
    

@app.get('/users/favorites/{user_name}',response_model= schemas.UserFavorites)
def get_user(user_name:str, db:Session=Depends(get_db)):
    user_db = db.query(models.user).filter_by(user_name=user_name).first()
    user_favorites_movies_db = db.query(models.user_movies_favorites).filter_by(user_id=user_db.id).all()
    movies_db = db.query(models.movies).all()
    user_favorites_series_db = db.query(models.user_series_favorites).filter_by(user_id=user_db.id).all()
    series_db = db.query(models.series).all()
    movies =[]
    series = []
    for favorite_movies in user_favorites_movies_db:
        for movie in movies_db:
            if movie.id == favorite_movies.id:
                movies.append(movie.name)
    for favorite_series in user_favorites_series_db:
        for movie in series_db:
            if movie.id == favorite_series.id:
                series.append(movie.name)
    
    respuesta = schemas.UserFavorites(movies=movies, series = series)
    return respuesta


@app.post('/user/create_user',response_model=schemas.Respuesta)
def add_user(entrada:schemas.User, db:Session=Depends(get_db)):
    print(entrada)
    user = models.user(
        user_name= entrada.user_name,
        firstName= entrada.firstName,
        lastName = entrada.lastName,
        password = entrada.password,
        )
    db.add(user)
    db.commit()
    db.refresh(user)
    respuesta = schemas.Respuesta(msj="funciona", error = "No Error")
    return respuesta

@app.get('/movies',response_model= List[schemas.MovieSerie])
def get_movies(db:Session=Depends(get_db)):
    movies_db = db.query(models.movies).all()    
    return movies_db

@app.post('/movies/create_movie',response_model=schemas.Respuesta)
def add_movie(entrada:schemas.CreatMovieSerie, db:Session=Depends(get_db)):
    movie = models.movies(
        name = entrada.name,
        director = entrada.director,
        averge_score = 0,
        )
    db.add(movie)
    db.commit()
    db.refresh(movie)
    respuesta = schemas.Respuesta(msj="funciona", error = "No Error")
    return respuesta

@app.get('/series',response_model= List[schemas.MovieSerie])
def get_series(db:Session=Depends(get_db)):
    series_db = db.query(models.series).all()    
    return series_db

@app.post('/series/create_serie',response_model=schemas.Respuesta)
def add_serie(entrada:schemas.CreatMovieSerie, db:Session=Depends(get_db)):
    serie = models.series(
        name = entrada.name,
        director = entrada.director,
        averge_score = 0,
        )
    db.add(serie)
    db.commit()
    db.refresh(serie)
    respuesta = schemas.Respuesta(msj="funciona", error = "No Error")
    return respuesta

@app.post('/user/movie_score/create',response_model=schemas.Respuesta)
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
    respuesta = schemas.Respuesta(msj="funciona", error = "No Error")
    return respuesta

@app.get('/movies_scores',response_model= List[schemas.Score])
def get_movies_score(db:Session=Depends(get_db)):
    response = []
       
    user_moive_score = db.query(models.user_movies_score).all()
    for score in user_moive_score:        
        response.append(schemas.Score(user_name=db.query(models.user).filter_by(id = score.user_id).first().user_name, 
                                      moive_serie_name=db.query(models.movies).filter_by(id = score.movies_id).first().name, 
                                      score=score.score, 
                                      description = score.description))
    return response

@app.post('/user/series_score/create',response_model=schemas.Respuesta)
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
    respuesta = schemas.Respuesta(msj="funciona", error = "No Error")
    return respuesta

@app.get('/series_scores',response_model= List[schemas.Score])
def get_series_score(db:Session=Depends(get_db)):
    response = []
    user_serie_score = db.query(models.user_series_score).all()
    for score in user_serie_score:
        response.append(schemas.Score(user_name=db.query(models.user).filter_by(id = score.user_id).first().user_name,
                                      moive_serie_name=db.query(models.series).filter_by(id = score.series_id).first().name,
                                      score=score.score,
                                      description = score.description))
    return response

@app.post('/user/movies_favorite/make',response_model=schemas.Respuesta)
def user_movies_favorites(entrada:schemas.UserMovieFavorite, db:Session=Depends(get_db)):
    user = db.query(models.user).filter_by(user_name=entrada.user_name).first()
    movie = db.query(models.movies).filter_by(name=entrada.movie_name).first()
    user_movies_favorites =  models.user_movies_favorites(user_id = user.id, movies_id = movie.id)
    db.add(user_movies_favorites)
    db.commit()
    db.refresh(user_movies_favorites)
    respuesta = schemas.Respuesta(msj="funciona", error = "No Error")
    return respuesta

@app.post('/user/series_favorite/make',response_model=schemas.Respuesta)
def user_series_favorites(entrada:schemas.UserSerieFavorite, db:Session=Depends(get_db)):
    user = db.query(models.user).filter_by(user_name=entrada.user_name).first()
    serie = db.query(models.series).filter_by(name=entrada.serie_name).first()
    user_series_favorites =  models.user_series_favorites(user_id = user.id, series_id = serie.id)
    db.add(user_series_favorites)
    db.commit()
    db.refresh(user_series_favorites)
    respuesta = schemas.Respuesta(msj="funciona", error = "No Error")
    return respuesta


