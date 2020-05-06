a = int(input())
count = 0
temp = [a]


def cal(a):
    list = []
    for i in a:
        list.append(i-1)
        if i % 3 == 0:
            list.append(i/3)
        if i % 2 == 0:
            list.append(i/2)
    return list


while True:
    if a == 1:
        print(count)
        break
    temp = cal(temp)
    count += 1
    if min(temp) == 1:
        print(count)
        break
