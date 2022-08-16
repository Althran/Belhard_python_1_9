"""
Написать класс FilmTypes, который будет наследоваться от Enum и содержать
константы-названия жанров фильмов.
"""
import enum


class FilmTypes(enum.Enum):
    ROMANCE_COMEDY = 'Romance_comedy'
    SCIENCE_FICTION = 'Science_fiction'
    HORROR = 'Horror'
    DOCUMENTARY = 'Documentary'
    ANIMATED = 'Animated'
    ANIMATION = 'Animation'
    THRILLER = 'Thriller'
    DRAMA = 'Drama'
    COMEDY = 'Comedy'
    ADVENTURE = 'Adventure'
