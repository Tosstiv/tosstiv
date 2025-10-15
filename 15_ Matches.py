import random


def start():
    print(f'################## Игра "15 спичек" ##################')
    print(f'Всего в куче 15 спичек')
    print(f'Каждый игрок по очереди берет от 1 до 3х спичек')
    print(f'Выигрывает тот, кто заберет последние спички из кучи!')
    print(f'######################################################\n')


def rnd_turn():
    print(f'Выбор очередности ходов: ')
    print(f'Введите 0, если ходить первым будет игрок')
    print(f'Введите 1, если ходить первым будет компьютер')
    print(f'Введите 2, чтобы выбрать очередность ходов случайным образом')
    while True:
        n = input('> ')
        if n.isdigit():
            n = int(n)
            if n > 2 or n < 0:
                print(f'Введите число 0, 1 или 2')
            else:
                if n == 2:
                    n = random.randint(0, 1)
                if n == 0:
                    print(f'Первым будет ходить игрок!')
                else:
                    print(f'Первым будет ходить компьютер!')
                break
        else:
            print(f'Вы ввели недопустимый символ. Введите число 0, 1 или 2')
    return n


def turn_player(matches):
    n = 4
    while n > 3 or n < 1:
        n = input('Сколько вы возьмете спичек? ')
        if n.isdigit():
            n = int(n)
            if n > 3 or n < 1:
                print(f'Вы вязли недопустимое количества спичек! Возьмите от 1 до 3х')
            if n > matches:
                print(f'Вы взяли больше чем осталось спичек!')
                n = 4
        else:
            print(f'Вы ввели недопустимые символы. Введите число от 1 до 3х')
            n = 4
    return n


def turn_ai(matches):
    n = matches % 4
    if n == 0:
        n = random.randint(1, 3)
    return n


matches = 15
count = 1
start()
turn = rnd_turn()
while True:
    print(f'\n******** Ход номер: {count} ********')
    if turn % 2 == 0:
        print(f'Ход игрока! Всего спичек: {matches}')
        n = turn_player(matches)
        print(f'Игрок взял спичек: {n}')
    elif turn % 2 == 1:
        print(f'Ход компьютера! Всего спичек: {matches}')
        n = turn_ai(matches)
        print(f'Компьютер взял спичек: {n}')
    matches -= n
    if matches == 0:
        if turn % 2 == 0:
            print(f'Победил игрок!')
        else:
            print(f'Победил компьютер!')
        break
    turn += 1
    count += 1

print('\n'*5)