x = int(input())
stick = [64]

while sum(stick) != x:
    
    tmp = stick.pop()/2
    stick.append(tmp)
    if sum(stick) >= x:
        continue
    stick.append(tmp)

print(len(stick))
