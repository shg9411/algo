def solution(logs):
    answer = set()
    check = dict()
    for log in logs:
        pid, num, score = log.split()
        if pid in check:
            check[pid][num] = score
        else:
            check[pid] = {num: score}
    haveToCheck = []
    for item in check:
        if len(check[item]) >= 5:
            haveToCheck.append(item)
    length = len(haveToCheck)
    for i in range(length):
        for j in range(i+1, length):
            if check[haveToCheck[i]] == check[haveToCheck[j]]:
                answer.add(haveToCheck[i])
                answer.add(haveToCheck[j])
    return sorted(answer) if answer else ["None"]
