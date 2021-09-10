from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, joinedload
from sqlalchemy.orm import Session

from .database import Base


class Director(Base):
    __tablename__ = "directors"

    id: int = Column(Integer, primary_key=True, index=True, nullable=False)
    name: str = Column(String, unique=True, index=True, nullable=False)


class Movie(Base):
    __tablename__ = "movies"

    id: int = Column(Integer, primary_key=True, index=True, nullable=False)
    title: str = Column(String, unique=True, nullable=False)
    imdb_id: str = Column(String, unique=True, index=True, nullable=False)
    year: int = Column(Integer, nullable=False)
    image_url: str = Column(String, nullable=False)
    imdb_rating: float = Column(Float, nullable=False)
    imdb_rating_count: str = Column(String, nullable=False)

    director_id: int = Column(Integer, ForeignKey("directors.id"), nullable=False)
    director: Director = relationship("Director")


def get_movies(db: Session, limit: int = 250):
    return (
        db.query(Movie)
        .options(joinedload(Movie.director))
        .order_by(Movie.imdb_rating.desc())
        .limit(limit)
        .all()
    )
