n = int(input())
count = n
for _ in range(n):
    alpha = [False]*26
    text = input()
    for i in range(len(text)):
        if not alpha[ord(text[i])-97]:
            alpha[ord(text[i])-97] = True
        elif text[i] == text[i-1]:
            continue
        else:
            count -= 1
            break
print(count)