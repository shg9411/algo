#from collections import OrderedDict

n,c = map(int,input().split())
frequency = dict()
numbers = list(map(int,input().split()))

for number in numbers:
    try:
        tmp = frequency[number]
        frequency[number]+=1
    except:
        frequency[number] = 1

tmp = sorted(frequency.items(),key=lambda x: x[1],reverse=True)

answer = ''

for t in tmp:
    for _ in range(t[1]):
        answer+=str(t[0])+' '
print(answer[:-1])