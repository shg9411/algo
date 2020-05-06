text = input()
joi = 0
ioi = 0
for i in range(len(text)-2):
    if text[i:i+3] == 'IOI':
        ioi+=1
    elif text[i:i+3] == 'JOI':
        joi+=1
print(joi)
print(ioi)