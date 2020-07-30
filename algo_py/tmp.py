import sys

a, b= map(str,sys.stdin.readline().split())
a_letter=list(a)
b_letter=list(b)

count_1 = 0
count_2 = 0
for i in range(len(a_letter)):
    # print(i,a_letter[i],b_letter[i])
    if (a_letter[i]!=b_letter[i]):
        count_1 += 1
for i in range(-len(a_letter),0):
    # print(i,a_letter[i],b_letter[i])
    if (a_letter[i]!=b_letter[i]):
        count_2 += 1

print(count_1<count_2 and count_1 or count_2)
