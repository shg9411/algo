def solution(day, k):
    date_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    weekend = (5, 6)
    answer = []
    for date in date_per_month:
        if (day+k-1) % 7 in weekend:
            answer.append(1)
        else:
            answer.append(0)
        day += date % 7
    return answer


day, k = 6, 25
print(solution(day, k))
