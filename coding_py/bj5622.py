alpha = input()
l = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'], [
    'M', 'N', 'O'], ['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]
sum = 3*len(alpha)
for i in range(len(alpha)):
    for j in range(len(l)):
        if alpha[i] in l[j]:
            sum +=j
            break

print(sum)