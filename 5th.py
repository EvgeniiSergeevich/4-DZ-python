# Даны два файла, в каждом из которых находится запись многочлена.
#  Задача - сформировать файл, содержащий сумму многочленов.
# В file1.txt :
# 2*x**2 + 4*x + 5
# В file2.txt:
# 4*x**2 + 1*x + 4
# Результирующий файл:
# 6*x**2 + 5*x + 9
from sympy import symbols
from math import prod

f1 = open('5_1.txt', "r")
f2 = open('5_2.txt', "r")
f3 = open('5_end.txt', 'w')

mnog1 = f1.read()
mnog2 = f2.read()
f1.close()
f2.close()

a = 0
b = 0
c = 0

a = int(mnog1[0]) + int(mnog2[0])                           # Работает только для квадратных уравнений
b = int(mnog1[9]) + int(mnog2[9])
c = int(mnog1[-1]) + int(mnog2[-1])
koeff = {a, b, c}
x = symbols('x')

mnog3 = str(sum(map(prod, zip(koeff, [x**i for i in range(3)]))))
f3.write(mnog3)
f3.close()