
import math

def kvadrat(a,b,c):
    D = math.sqrt(b**2-4*a*c)
    if D >= 0:
        x = (-b+D)/(2*a)
        y = (-b-D)/(2*a)
        return f'Корни {x}, {y}'
    else:
        return 'Решений нет'

try:
    a = float(input('A: '))
    b = float(input('B: '))
    c = float(input('C: '))
    print(kvadrat(a,b,c))
except:
    print('Аргумент должен быть числом')
