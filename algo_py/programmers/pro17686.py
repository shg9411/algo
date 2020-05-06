import re

def solution(files):
    temp = [re.split(r"([0-9]+)",file) for file in files]
    sort = sorted(temp,key = lambda x : (x[0].lower(),int(x[1])))
    return ["".join(s) for s in sort]

files = ['F-0050510 Freedom Fighter', 'B-0050 Superfortress',
         'A-010 Thunderbolt II', 'F-005059 Freedom Fighter']

print(solution(files))
