# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
#  многочлена и записать в файл многочлен степени k.

# Пример:

# k=2 => 2*x*2 + 4*x + 5 = 0 или x2 + 5 = 0 или 10*x*2 = 0
# k=3 => 2*x*3 + 4*x*2 + 4*x + 5 = 0 5'. 

from random import randint
from sympy import symbols
from math import prod

k = int(input('Введите степень k от 0 до 100: '))
koeff = [randint(-100, 100) for i in range(k)] + [randint(1, 100)]      # Генерирую коэффициенты
x = symbols('x')

mnog = str(sum(map(prod, zip(koeff, [x**i for i in range(k + 1)]))))    # Создаю многочлен
mnog = mnog + " = 0"                                                    
print(mnog)
f = open('4th_text.txt', 'w')                                           # Записываю в файл уравнение
f.writelines(mnog)
f.close()