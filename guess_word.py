#числовая угадайка
from random import *
print(f'Добро пожаловать в числовую угадайку')

def is_valid(t: str):
    return t.isdigit() and 1 <= int(t) <= 100

def max_range():
    while True:
        r = input(f'\nЗадайте максимальное число?\n')
        if not r.isdigit() or int(r) < 1:
            print('Введите целое число больше нуля!\n')
            continue
        return int(r)

r = max_range()
random_number = randint(1, r)

def user_number():
    while True:
        n = (input(f'Введите число от 1 до {r}:\n'))
        if is_valid(n) and 1 <= int(n) <= r:
             return int(n)
        print(f'Может быть все-таки введем целое число?')

def game():
    n, attempts = 0, 1
    while n !=  random_number:
        n = user_number()
        if n < random_number:
            print(f'Ваше число меньше загаданного, попробуйте еще разок')
            attempts += 1
        elif n > random_number:
            print(f'Ваше число больше загаданного, попробуйте еще разок')
            attempts += 1
        else:
            print(f'Вы угадали, поздравляем!\nЗагаданное число - {random_number}\nКоличество попыток: {attempts}!')

while True:
    game()
    print('Отличная игра, еще разок?')
    ans = input('Да(Д) или Yes(Y) если желаете продолжить: ')
    if ans.lower() in ('д', 'да', 'yes', 'y'):
        r = max_range()
        random_number = randint(1, r)
        continue
    else:
        break
print()
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')  



