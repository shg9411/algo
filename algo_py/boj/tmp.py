n = int(input())
count = 0
for _ in range(n):
    alpha = set()
    text = input()
    alpha.add(text[0])
    f = 1
    for i in range(1,len(text)):
        if text[i] == text[i-1]:
            continue
        else:
            if text[i] not in alpha:
                alpha.add(text[i])
            else:
                f = 0
                break
    if f:
        count+=1
print(count)