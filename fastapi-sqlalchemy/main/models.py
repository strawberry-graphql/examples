from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, joinedload
from sqlalchemy.orm import Session

from .database import Base


class Director(Base):
    __tablename__ = "directors"

    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String, unique=True, index=True)


class Movie(Base):
    __tablename__ = "movies"

    id: int = Column(Integer, primary_key=True, index=True)
    title: str = Column(String, unique=True)
    imdb_id: str = Column(String, unique=True, index=True)
    year: int = Column(Integer)
    image_url: str = Column(String)
    imdb_rating: float = Column(Float)
    imdb_rating_count: str = Column(String)

    director_id: int = Column(Integer, ForeignKey("directors.id"))
    director: Director = relationship("Director")


def get_movies(db: Session, limit: int = 250):
    return (
        db.query(Movie)
        .options(joinedload(Movie.director))
        .order_by(Movie.imdb_rating.desc())
        .limit(limit)
        .all()
    )
