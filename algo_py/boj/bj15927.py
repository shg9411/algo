string = input()
ans = -1
if string != string[::-1]:
    ans = len(string)
else:
    if len(set(string)) != 1:
        ans = len(string)-1
print(ans)
