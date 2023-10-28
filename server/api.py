#api.py
import sqlalchemy
from models import Artists, Albums, Tracks
from database import session
from fastapi import FastAPI
from sqlalchemy import select, func, update



app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello World"}

@app.get("/albums/")
async def getAlbum(artist_id: int):

    statement = select(Albums).join(Albums.artists).where(Artists.artistId == artist_id)
    responses = tuple(session.scalars(statement).all())

    return responses

@app.get("/artists/")
async def getArtist(artist_name: str):

    name = f"%{artist_name}%"
    responses = tuple(session.query(Artists).filter(func.lower(Artists.name).like(name.lower())).all())

    return responses

@app.get("/tracks/")
async def getTracks(album_id: int):

    statement = select(Tracks).join(Tracks.albums).where(Albums.albumId == album_id)
    responses = tuple(session.scalars(statement).all())

    return responses

session.close()
