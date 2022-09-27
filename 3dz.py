X = int(input('Введите координату X: '))
Y = int(input('Введите координату Y: '))
if (X > 0 and Y > 0):
    print('1 четверть')

elif ( X > 0 and 0 > Y):
    print('2 четверть')

elif (X < 0 and 0 > Y):
    print('3 четверть')

elif (X < 0 and Y > 0):
    print('4 четверть')
