import re
input()
print(sum(map(int,filter(None,re.split('[a-zA-Z]',input().rstrip())))))
