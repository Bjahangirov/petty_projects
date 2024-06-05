#Генератор паролей
import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
chars = ''
#---------------------------------------------------
#---Запрос данных
password_count = int(input('Укажите количество паролей\n'))
password_length = int(input('Укажите длину одного пароля\n'))
flag_numbers = input('Включать ли цифры в пароли?\n Если ДА - напишите "Y", если НЕТ - любую другую клавишу.\n')
flag_prime_AZ = input('Включать ли буквы A-Z в пароли?\n Если ДА - напишите "Y", если НЕТ - любую другую клавишу.\n')
flag_lowcase_az = input('Включать ли буквы a-z в пароли?\n Если ДА - напишите "Y", если НЕТ - любую другую клавишу.\n')
flag_symbols = input('Включать ли буквы символы в пароли?\n Если ДА - напишите "Y", если НЕТ - любую другую клавишу.\n')
flag_missunderstandings = input('Исключать ли неоднозначные символы il1Lo0O в пароли?\n')
#---------------------------------------------------
if flag_numbers.lower() == 'y':
    chars += digits
if flag_prime_AZ.lower() == 'y':
    chars += uppercase_letters
if flag_lowcase_az.lower() == 'y':
    chars += lowercase_letters
if flag_symbols.lower() == 'y':
    chars += punctuation
if flag_missunderstandings == 'y':
    for i in 'il1Lo0O':
        chars = chars.replace(i, '')
#---------------------------------------------------
# Функция генерации пароля на основании данных

def generate_password(length, char):
    password = ''
    for i in range(length):
        password += random.choice(char)
    print(password)
#---------------------------------------------------
print()
print('Сгенерированные пароли:')
print()
#---------------------------------------------------
# Вызов функции генерации
for i in range(password_count):
    generate_password(password_length, chars)
#---------------------------------------------------
