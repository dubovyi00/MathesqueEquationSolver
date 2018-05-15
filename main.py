import linear
from linear import *

equat = input(" EquationSolver build alpha-1 \n Введите уравнение: ")

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
    equatLinear(equat, lit)

elif err:
    print('Равенство не может быть решено')
