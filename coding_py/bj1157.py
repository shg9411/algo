s = input().upper()
x = list(set(s))
d = dict()
for i in range(len(x)):
    d[x[i]] = s.count(x[i])
mx = max(d.values())
many = []
for key in d.keys():
    if mx == d.get(key):
        many.append(key)
if len(many)>1:
    print('?')
else:
    print(many[0])
