import sys

num = int(sys.stdin.readline())
ropes = []
for i in range(num):
    ropes.append(int(sys.stdin.readline()))
ropes.sort(reverse=True)

def ropeMax(List):
    max = 0
    for i in range(num):
        if ((i+1)*List[i] > max):
            max =  (i+1)*List[i]
    return max
print(ropeMax(ropes))