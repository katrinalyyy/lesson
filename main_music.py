import os.path
import pickle
from typing import List


class Music:
def __init__(self, id: int, name:str, author:str, genre: str, year: int, duration: str):
        self.id = id
        self.name = name
        self.author = author
        self.genre = genre
        self.year = year
        self.duration = duration

