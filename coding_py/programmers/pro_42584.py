def solution(prices):
    answer = [0 for _ in range(len(prices))]
    stack = []
    for i in range(len(prices)-2,-1,-1):
        day = 0
        while stack and stack[-1][0]>=prices[i]:
            day += stack.pop()[1]
        stack.append([prices[i],day+1])
        answer[i] = stack[-1][1]
    return answer

prices = [1,2,3,2,3]
print(solution(prices))