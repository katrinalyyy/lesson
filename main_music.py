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


class Audioteka:
    def __init__(self):
        self.music: List[Music] = []

    def load_music(self, music: List[Music]):
        self.music = music

    def add_music(self, name: str, author: str, genre: str, year: int, duration: str):
        id = 1
        if self.music:
            id = self.music[-1].id + 1
        self.music.append(Music(id, name, author, genre, year, duration))

    def get_list_songs(self):
        for music in self.music:
            print(music)
        print('--------------')

    def find_music_by_id(self, input_id: int):
        for i in self.music:
            if i.id == input_id:
                print(i)
        print('--------------')

    def find_music_by_name(self, input_name: str):
        for i in self.music:
            if i.name == input_name:
                print(i)
        print('--------------')

    def find_music_by_genre(self, input_genre: str):
        for i in self.music:
            if i.genre == input_genre:
                print(i)
        print('--------------')

    def find_music_by_author(self, input_author: str):
        for i in self.music:
            if i.author == input_author:
                print(i)
        print('--------------')

    def find_music_by_year(self, input_year: int):
        for i in self.music:
            if i.year == input_year:
                print(i)
        print('--------------')

    def max_duration_song(self):
        max_duration = int(self.music[0].duration.split(':')[0]) * 60 + int(self.music[0].duration.split(':')[1])
        result_music = self.music[0]
        for i in range(len(self.music)):
            if int(self.music[i].duration.split(':')[0]) * 60 + int(
                    self.music[i].duration.split(':')[1]) > max_duration:
                max_duration = int(self.music[i].duration.split(':')[0]) * 60 + int(
                    self.music[i].duration.split(':')[1])
                result_music = self.music[i]
        print(result_music)

    def min_duration_song(self):
        min_duration = int(self.music[0].duration.split(':')[0]) * 60 + int(self.music[0].duration.split(':')[1])
        result_music = self.music[0]
        for i in range(len(self.music)):
            if int(self.music[i].duration.split(':')[0]) * 60 + int(
                    self.music[i].duration.split(':')[1]) < min_duration:
                min_duration = int(self.music[i].duration.split(':')[0]) * 60 + int(
                    self.music[i].duration.split(':')[1])
                result_music = self.music[i]
        print(result_music)


def load_data(audioteka: Audioteka):
    if os.path.exists('database_music.dat'):
        with open('database_music.dat', 'rb') as f:
            size = pickle.load(f)
            music = []
            for i in range(size):
                music.append(pickle.load(f))
            audioteka.load_music(music)
    else:
        with open('database_music.dat', 'wb') as f:
            pickle.dump(0, f)
    return audioteka


def save(file_name: str, data: List):
    with open(file_name, 'wb') as f:
        pickle.dump(len(data), f)
        for item in data:
            pickle.dump(item, f)


def main():
    audioteka = load_data(Audioteka())
    ok = False
    while not ok:
        print('''Постижимые команды:
        1) - Добавить песню в аудиотеку
        2) - Вывести список всех песен
        3) - Найти музыку
        4) - Самая длинная песня
        5) - Самая короткая песня
        0) - Выход''')
        cmd = input('Введите номер команды: ')
        if cmd == '0':
            ok = True
        elif cmd == '1':
            try:
                name = input('Название песни:')
                author = input('Автор/авторка песни:')
                genre = input('Жанр песни:')
                year = int(input('Год выпуска песни:'))
                duration = input('Длительность песни:')
                audioteka.add_music(name, author, genre, year, duration)
                save('database_music.dat', audioteka.music)
            except ValueError:
                print('ЧТО-ТО ПОШЛО НЕ ТАК')
        elif cmd == '2':
            audioteka.get_list_songs()
        elif cmd == '3':
            print()
            print('''Какую именно музыку найти:
                    1) - по айди
                    2) - по названию
                    3) - по автору
                    4) - по жанру
                    5) - по году''')
            print()
            try:
                poisk = int(input('Введите номер команды: '))
                print()
                if poisk == 1:
                    audioteka.find_music_by_id(int(input('Введите id: ')))
                elif poisk == 2:
                    audioteka.find_music_by_name(input('Введите название: '))
                elif poisk == 3:
                    audioteka.find_music_by_author(input('Введите автора: '))
                elif poisk == 4:
                    audioteka.find_music_by_genre(input('Введите жанр: '))
                elif poisk == 5:
                    audioteka.find_music_by_year(int(input('Введите год: ')))
            except ValueError:
                print('МОЯ ЛЮБИМАЯ ПЕСНЯ - Blue moon ($NOT)')
        elif cmd == '4':
            audioteka.max_duration_song()
        elif cmd == '5':
            audioteka.min_duration_song()
    print()


if __name__ == '__main__':
    main()
