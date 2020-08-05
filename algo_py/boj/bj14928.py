x = input()
res = 0
for num in x:
    res = (res*10+int(num)) % 20000303
print(res)