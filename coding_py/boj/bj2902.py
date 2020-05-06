s = input()
result = ""
for i in range(len(s)):
    if s[i].isupper():
        result+=s[i]
print(result)