maxNum = 1004001
x = [True for i in range(maxNum+1)]
x[0] = x[1] = False

for i in range(2, int(maxNum**0.5)+1):
    if x[i]:
        for j in range(i*2, maxNum+1, i):
            x[j] = False

prime = [v for v in range(int(input()), maxNum+1) if x[v]]

for num in prime:
    if str(num) == str(num)[::-1]:
        print(num)
        break
