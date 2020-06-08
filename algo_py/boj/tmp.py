result = 0
for i in range(int(input())):
    word = input()
    for char in word:
        print(word.find(char),end=' ')
print(result)
