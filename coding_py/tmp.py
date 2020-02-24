data = input()
result = 0
for i in range(len(data)):
    for j in range(i,len(data)+1):
        try:
            results = eval(data[:i] + '(' + data[i:j] + ')' + data[j:])
            result = min(result,results)
        except Exception as ex:
            continue
print(result)