import os.path
import pickle
from typing import List


class Music:
    def __init__(self, id: int, name: str, author: str, genre: str, year: int, duration: str):
        self.id = id
        self.name = name
        self.author = author
        self.genre = genre
        self.year = year
        self.duration = duration


class Audioteka:
    def __init__(self):
        self.books: List[Music] = []

    def load_music(self, music: List[Music]):
        self.music = music


def load_data(library: Audioteka):
    if os.path.exists('database_users.dat'):
        with open('database_music.dat', 'rb') as f:
            size = pickle.load(f)
            music = []
            for i in range(size):
                music.append(pickle.load(f))
            library.load_music(music)
    else:
        with open('database_music.dat', 'wb') as f:
            pickle.dump(0, f)


def save(file_name: str, data: List):
    with open(file_name, 'wb') as f:
        pickle.dump(len(data), f)
        for item in data:
            pickle.dump(item, f)


