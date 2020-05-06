def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)

number = '9999'
number2 = '1231234'
k = 2
k2 = 3

print(solution(number,k))
print(solution(number2,k2))