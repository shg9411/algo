testcase=int(input())

for i in range(testcase):
    num=int(input())
    count = 0
    while 1:
        if 5 > num:
            break
        num//=5
        count += num
        

    print(count)