import pickle


class stud:
    fam = None
    surn = None
    name = None
    bal = None


f = open('students.dat', 'rb')
St = pickle.load(f)
while True:
    print("Введите номер операции с БД'шкой:")
    print('1 - сортировка БД по убыванию балла')
    print('2 - поиск в БД студентов, имеющих двойки')
    print('3 - редактирование БД')
    print('4 - печать БД')
    print('5 - Выход')
    num = int(input())
    if num == 1:
        St.sort(key=lambda x: sum(x.bal) / len(x.bal), reverse=True)
        for i in St:
            print(i.fam, i.name, i.surn)
    elif num == 2:
        for i in St:
            if 2 in i.bal:
                print(i.fam, i.name, i.surn)
    elif num == 3:
        print('Введите цель поражения (студента):')
        sn = input()
        print('Введите нового студента и 5 оценок через пробел:')
        x = input()
        for i in St:
            if i.fam == sn:
                x = x.split(' ', 3)
                i.fam = x[0]
                i.name = x[1]
                i.surn = x[2]
                i.bal = list(map(int, x[3].split()))
    elif num == 4:
        for i in St:
            print(i.fam, i.name, i.surn, *i.bal)
        print('---------')
    elif num == 5:
        v = input('Выйти или не выйти??? Вот в чём вопрос!(Yes/No)')
        if v == 'Yes' or v == 'yes':
            break
