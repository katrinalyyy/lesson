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


    def __str__(self):
        return f'{self.id} - "{self.name}" {self.author} {self.genre} {self.year} {self.duration}'


def add_music(self):
        pass

def get_list_songs(self):
        pass

def find_music_by_id(self):
        pass

def find_music_by_genre(self):
        pass

def find_music_by_author(self):
        pass

def find_music_by_year(self):
        pass

def max_duration_song(self):
        pass

def min_duration_song(self):
        pass


def main():
    audioteka = load_data(Audioteka())
    ok = False
    while not ok:
        print('''Постижимые команды:
        1) - Добавить песню в аудиотеку
        2) - Вывести список всех песен
        3) - Найти музыку
        4) - Самая длинная песня
        5) - Самая короткая песня''')
        cmd = input('Введите номер команды: ')
        if cmd == '0':
            end = True
        elif cmd == '1':



if __name__ == '__main__':
    main()