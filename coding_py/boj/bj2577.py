tmp = int(input())*int(input())*int(input())
li = [0] * 10
for i in str(tmp):
    li[int(i)] += 1
for i in li:
    print(i)