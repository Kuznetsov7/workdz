from xml.dom.expatbuilder import ElementInfo


Number = int(input('Введите четверть: '))
X = 1,2,3,4,5
X1 = -1,-2,-3,-4,-5
Y = 1,2,3,4,5,6
Y1 = -1,-2,-3,-4,-5,-6
if Number == 1:
    print( 'X =  ' , X , ' Y = ', Y )
elif Number == 2:
     print( 'X =  ' , X1 , ' Y = ', Y )
elif Number == 3:
     print( 'X =  ' , X1 , ' Y = ', Y1 )
elif Number == 4:
     print( 'X =  ' , X , ' Y = ', Y1 )
else:
    print('Такой четверти нет')
