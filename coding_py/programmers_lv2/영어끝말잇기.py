def solution(n, words):
    count = -1
    word_set = set()
    tmp = words[0][0]
    for w in words:
        count+=1
        print(tmp)
        if w in word_set or w[0]!=tmp:
            return [count%n+1, count//n+1]
        word_set.add(w)
        tmp = w[-1]
    return [0,0]

print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))