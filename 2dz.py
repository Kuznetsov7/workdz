print('x y Z')
for x in range(2):
    for y in range(2):
        Z = x or y
        print(x , y , bool(Z)) 
