X = int(input('Введите координату X: '))
Y = int(input('Введите координату Y: '))
X1 = int(input('Введите координату X1: '))
Y1 = int(input('Введите координату Y1: '))
num = float((X1-X)**2 +(Y1-Y) **2)
import math
grug = math.sqrt(num)
print( "Расстояние между точками: " , round(grug, 2) )