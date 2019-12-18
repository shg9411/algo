import sys

alpha = [0]*26

for line in sys.stdin:
    tmp = line.split()
    for word in tmp:
        for char in word:
            alpha[ord(char)-97] += 1

for i in range(26):
    if alpha[i]==max(alpha):
        print(chr(i+97),end='')
