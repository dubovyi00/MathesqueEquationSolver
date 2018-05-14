equat = input(" EquationSolver build alpha-1 \n Введите уравнение (подсказка: умножение числа на переменую писать без знака умножения!)\n")

lit = ''
err = False
eqIsThere = False
litIsThere = False

for i in equat:
    if i.isalpha():
        if lit == '':
            lit = i
            litIsThere = True
        elif lit != '' and lit != i:
            print('Ошибка ввода: в уравнении больше одной переменной')
            err = True
    if i == '=':
        if not eqIsThere:
            eqIsThere = True
        elif eqIsThere:
            print('Ошибка ввода: слишком много знаков равно')
            err = True

if not eqIsThere:
    print('Ошибка ввода: знак равенства отсутствует')
    err = True

if not litIsThere:
    print('Ошибка ввода: отсутствует переменная')
    err = True

if not err:
    left = ''
    right = ''
    eqIsThere = False
    for i in equat:
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
        litIsThere = False
        ch = ''
        for i in left:
            if i == '+' or i == '-':
                if num == 0:
                    ch = i
                elif num != 0:
                    if litIsThere:
                        a += num
                        litIsThere = False
                    elif not litIsThere:
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
                    elif ch != '':
                        num = 1
                        litIsThere = True
                elif num != 0:
                    litIsThere = True
        if num != 0:
            if litIsThere:
                a += num
                litIsThere = False
            elif not litIsThere:
                b += num
        num = 0
        ch = ''
        litIsThere = False

        for i in right:
            if i == '+' or i == '-':
                if num == 0:
                    ch = i
                elif num != 0:
                    if litIsThere:
                        a -= num
                        litIsThere = False
                    elif not litIsThere:
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
                    litIsThere = True
                elif num != 0:
                    litIsThere = True
        if num != 0:
            if litIsThere:
                a -= num
                litIsThere = False
            elif not litIsThere:
                b -= num

        print('Решение:')
        print('Переносим все члены уравнения в правую часть и складываем подобные члены')
        if b > 0:
            print('{0}{1} + {2} = 0'.format(a,lit,b))
        elif b == 0:
            print('{0}{1} = 0'.format(a,lit))
        elif b < 0:
            print('{0}{1} - {2} = 0'.format(a,lit,-b))

        if a == 0:
            if b == 0:
                print('В данном случае, корнем уравнения является любое число')
            elif b != 0:
                b *= (-1)
                print('Приводим выражение к виду ax = -b')
                if b > 0:
                    print('{0}{1} = {2}'.format(a,lit,b))
                elif b < 0:
                    print('{0}{1} = {2}'.format(a,lit,-b))
                print('Уравнение не имеет корней, так как выражение (-b : a) при a = 0 и b != 0 не имеет смысла')
        elif a != 0:
            if b > 0:
                print('Приводим выражение к виду a{0} = -b'.format(lit))
                print('{0}{1} = {2}'.format(a,lit,b))
            elif b < 0:
                print('Приводим выражение к виду a{0} = -b'.format(lit))
                print('{0}{1} = {2}'.format(a,lit,-b))
            rez = -b / a
            print('Корень уравнения: {0} = {1}'.format(lit,rez))

elif err:
    print('Равенство не может быть решено')
