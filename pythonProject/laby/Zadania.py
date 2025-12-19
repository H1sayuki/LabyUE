from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, Session, declarative_base

DATABASE_URL = "sqlite:///filmy.db"
Base = declarative_base()
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)


class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    genres = Column(String)


class Link(Base):
    __tablename__ = "links"
    movie_id = Column(Integer, primary_key=True)
    imdb_id = Column(String)
    tmdb_id = Column(String)


class Rating(Base):
    __tablename__ = "ratings"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer)
    movie_id = Column(Integer)
    rating = Column(Float)
    timestamp = Column(Integer)


class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer)
    movie_id = Column(Integer)
    tag = Column(String)
    timestamp = Column(Integer)


Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/movies")
def get_movies(db: Session = Depends(get_db)):
    movies = db.query(Movie).all()
    return movies


@app.get("/links")
def get_links(db: Session = Depends(get_db)):
    return db.query(Link).all()


@app.get("/ratings")
def get_ratings(db: Session = Depends(get_db)):
    return db.query(Rating).limit(100).all()


@app.get("/tags")
def get_tags(db: Session = Depends(get_db)):
    return db.query(Tag).all()
