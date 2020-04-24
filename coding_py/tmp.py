x = int(input())
for i in range(x):
    y = 0
    
    for i in input():
        if i == '(':
            y += 1
        elif i == ')':
            y-= 1
            if y<0:
                print('NO')
                break
    if y == 0:
        print('YES')
    else:
        print('NO')