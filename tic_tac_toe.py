print('Приветствую, это игра Крестики-нолики! :) ')
again = 'Y'
while again.upper() == 'Y':
    m = [[0]*3 for i in range(3)]
    m = [[(i*3+j + 1) for j in range(3)] for i in range(3)]
    print('Игрок 1! Ваша сторона: X. Вы ходите первым. \n')
    print('Игрок 2! Ваша сторона: О!\n')
    storona_X = 'X'
    storona_O = 'O'
    print('-' * 45)
    [print(' ' * 15, *w) for w in m]
    print('-' * 45)
    
    def pat():
        print('Ничья')
    
    def winner(matrix):
        x, o = 'X', 'O' #
        w_main_diag = []
        w_comman_diag = []
        for i in range(3):
            for j in range(3):
                if i == j:
                    w_main_diag.append(matrix[i][i])
                if j== 3-i-1:
                    w_comman_diag.append(matrix[i][j])
                    
        if len(set(w_main_diag)) == 1 and ''.join([str(i) for i in set(w_main_diag)]) == 'X':       
            print('Победил Игрок Х!')
            return True
        elif ''.join([str(i) for i in set(w_main_diag)]) == 'O':
            print('Победил Игрок O!')
            return True
            
        if len(set(w_comman_diag)) == 1 and ''.join([str(i) for i in set(w_comman_diag)]) == 'X':
            print('Победил Игрок Х!')
            return True
            
        elif ''.join([str(i) for i in set(w_comman_diag)]) == 'O':
            print('Победил Игрок O!')
            return True
            
        for i in matrix:
            if len(set(i)) == 1 and ''.join([str(i) for i in set(i)]) == 'X':
                print('Победил Игрок Х!')
                return True
                
            elif ''.join([str(i) for i in set(i)]) == 'O':
                print('Победил Игрок O!')
                return True
            
        Transp = [i for i in zip(*matrix)]
        country = 0
        for el in Transp:
            if len(set(el)) == 1 and ''.join([str(i) for i in set(el)]) == 'X':
                country += 1
        if country == 1:
            print('Победил Игрок Х!')
            return True
            
        elif ''.join([str(i) for i in set(el)]) == 'O':
            print('Победил Игрок O!')
            return True
        
        return False
    
    Flag = 'X'
    if storona_X in ['O', 'o', 0]:
        Flag = 'O'
    elif storona_X in ['X', 'x']:
        Flag = 'X'
    if storona_O in ['O', 'o', 0]:
        Flag = 'O'
    elif storona_O in ['X', 'x']:
        Flag = 'X'
    
    counter = 0
    
    while winner(m) != True:
        for i in range(1,10):
            if i % 2 != 0:
                Flag = 'X'
                print('Ход Игрока Х.')
                num = int(input())
                #if num not in m:
                #   print('такой ячейки нет или занято!')
                for i in range(3):
                    for j in range(3):
                        if m[i][j] == num:
                            m[i][j] = Flag
                            counter += 1
                print('-' * 45)
                [print(' ' * 15, *w) for w in m]
                print('-' * 45)
                if winner(m) == True: break
            else:
                Flag = 'O'
                print('Ход Игрока О.')
                num = int(input())
                #if num not in m: print('такой ячейки нет или занято!')
                for i in range(3):
                    for j in range(3):
                        if m[i][j] == num:
                            m[i][j] = Flag
                            counter += 1
                print('-' * 45)
                [print(' ' * 15, *w) for w in m]
                print('-' * 45)
                winner(m)
                if winner(m) == True: break
        if winner(m) == True:
            break
        for i in m:
            for j in i:
                if str(j) == j.isdigit():
                    continue
                else:
                    flazhok = None
        if flazhok == None:
            pat()
            break
    again = input('Хотите сыграть еще? Нажмите "Y" для игры с начала.\n')
print('В таком случае удачи и хорошего дня!')



