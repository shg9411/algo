def solution(gems):
    x = 0
    y = length = len(gems)
    gem = set(gems)
    tmp = set()
    tmpDict = dict()
    i = j = 0
    while j < length:
        if len(tmp) == len(gem):
            while tmpDict[gems[i]] > 1:
                tmpDict[gems[i]] -= 1
                i += 1
            if j-i < y-x:
                x = i
                y = j
        tmp.add(gems[j])
        try:
            tmpDict[gems[j]] += 1
        except:
            tmpDict[gems[j]] = 1
        j += 1

    return [x+1, y]


gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))
