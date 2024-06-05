
print('Добро пожаловать. Вас приветствует KАЛЬКУЛЯТОР.\n')
prodolzhit = 'Y'
while prodolzhit == 'Y' or prodolzhit == 'y':
    chislo_1 = float(input('Введите первое число:\n'))
    operacia = input('Введите знак операции (+, -, /, *):\n') 
    chislo_2 = float(input('Введите второе число:\n'))
    if operacia == '+':
        print('ОТВЕТ:', chislo_1 + chislo_2)
    elif operacia == '-':
        print('ОТВЕТ:', chislo_1 - chislo_2)
    elif operacia == '*' or operacia == 'x' or operacia == 'х':
        print('ОТВЕТ:', chislo_1 * chislo_2)
    elif operacia == '/' or operacia == '//':
        print('ОТВЕТ:', chislo_1 // chislo_2)
    elif operacia == '**' or operacia == '^':
        print('ОТВЕТ:', chislo_1 ** chislo_2)
    else : 
        print('ОШИБКА! Некорректный знак операции.\n')
    prodolzhit = input('Введите "Y", чтобы ПРОДОЛЖИТЬ или любую другую клавишу, чтобы ЗАВЕРШИТЬ\n')

    
