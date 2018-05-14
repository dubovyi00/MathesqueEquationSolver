def equatLinear(equation,var):
    left = ''
    right = ''
    eqIsThere = False
    litisthere = False
    err = False
    ch = ''
    for i in equation:
        if i == '=':
            eqIsThere = True
        if not eqIsThere and i != ' ' and i != '=':
            left += i
        elif eqIsThere and i != ' ' and i != '=':
            right += i
    if left == '' or right == '':
        print('Ошибка ввода: до/после знака равно отсутствуют какие-либо числа или переменные')
        err = True
    if err:
        print('Равенство не может быть решено')
    elif not err:
        a = 0
        b = 0
        num = 0
        litisthere = False
        ch = ''
        for i in left:
            if i == '+' or i == '-':
                if num == 0:
                    ch = i
                elif num != 0:
                    if litisthere:
                        a += num
                        litisthere = False
                    elif not litisthere:
                        b += num
                    ch = i
                    num = 0
            if i.isdigit():
                if i == '0':
                    if num != 0:
                        num = num * 10
                    elif num == 0:
                        ch = ''
                elif i != '0':
                    if num == 0:
                        if ch == '+' or ch == '':
                            num = int(i)
                        elif ch == '-':
                            num = -1 * int(i)
                    elif num != 0:
                        if ch == '+' or ch == '':
                            num = num * 10 + int(i)
                        elif ch == '-':
                            num = num * 10 - int(i)
            if i.isalpha():
                if num == 0:
                    if ch == '':
                        pass
                    elif ch == '+':
                        num = 1
                        litisthere = True
                    elif ch == '-':
                        num = -1
                        litisthere = True
                elif num != 0:
                    litisthere = True
        if num != 0:
            if litisthere:
                a += num
                litisthere = False
            elif not litisthere:
                b += num
        num = 0
        ch = ''
        litisthere = False

        for i in right:
            if i == '+' or i == '-':
                if num == 0:
                    ch = i
                elif num != 0:
                    if litisthere:
                        a -= num
                        litisthere = False
                    elif not litisthere:
                        b -= num
                    ch = i
                    num = 0
            if i.isdigit():
                if i == '0':
                    if num != 0:
                        num = num * 10
                    elif num == 0:
                        ch = ''
                elif i != '0':
                    if num == 0:
                        if ch == '+' or ch == '':
                            num = int(i)
                        elif ch == '-':
                            num = -1 * int(i)
                    elif num != 0:
                        if ch == '+' or ch == '':
                            num = num * 10 + int(i)
                        elif ch == '-':
                            num = num * 10 - int(i)
            if i.isalpha():
                if num == 0:
                    num = 1
                    litisthere = True
                elif num != 0:
                    litisthere = True
        if num != 0:
            if litisthere:
                a -= num
                litisthere = False
            elif not litisthere:
                b -= num

        print('Решение:')
        print('Переносим все члены уравнения в правую часть и складываем подобные члены')
        if b > 0:
            print('{0}{1} + {2} = 0'.format(a, var, b))
        elif b == 0:
            print('{0}{1} = 0'.format(a, var))
        elif b < 0:
            print('{0}{1} - {2} = 0'.format(a, var, -b))

        if a == 0:
            if b == 0:
                print('В данном случае, корнем уравнения является любое число')
            elif b != 0:
                b *= (-1)
                print('Приводим выражение к виду ax = -b')
                if b > 0:
                    print('{0}{1} = {2}'.format(a, var, b))
                elif b < 0:
                    print('{0}{1} = {2}'.format(a, var, -b))
                print('Уравнение не имеет корней, так как выражение (-b : a) при a = 0 и b != 0 не имеет смысла')
        elif a != 0:
            if b > 0:
                print('Приводим выражение к виду a{0} = -b'.format(var))
                print('{0}{1} = {2}'.format(a, var, b))
            elif b < 0:
                print('Приводим выражение к виду a{0} = -b'.format(var))
                print('{0}{1} = {2}'.format(a, var, -b))
            rez = -b / a
            print('Корень уравнения: {0} = {1}'.format(var, rez))
