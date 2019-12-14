
class Stack(list):
    push = list.append

    def is_empty(self):
        if not self:
            return True
        else:
            return False

    def peek(self):
        return self[-1]


def solution(input):
    bracket = {'[': 3, '{': 2, '(': 1, ')': -1, '}': -2, ']': -3}
    tmp = list(c for c in list(input) if c in [
        '[', '{', '(', ')', '}', ']'])
    stack = Stack()
    if len(tmp)==0:
        return True
    stack.push(tmp.pop(0))
    while len(tmp) > 0:
        if stack.is_empty():
            stack.push(tmp.pop(0))
            continue
        fromStack = stack.peek()
        fromInput = tmp.pop(0)
        if bracket.get(fromStack)+bracket.get(fromInput) == 0 and bracket.get(fromStack) > bracket.get(fromInput):
            stack.pop()
        elif abs(bracket.get(fromStack)) > abs(bracket.get(fromInput)):
            stack.push(fromInput)
        else:
            return False
    return stack.is_empty()


print(solution("[][[[[[[[[]]]]]]]]"))
