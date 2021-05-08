def solution(s):
    num = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
           'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    answer = s
    for i, j in num.items():
        answer = answer.replace(i, j)
    return answer


s = "123"
print(solution(s))
