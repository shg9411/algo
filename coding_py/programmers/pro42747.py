def solution(citations):
    ex = False
    for h in range(max(citations),0,-1):
        over_h = 0
        for citation in citations:
            if citation>=h:
                over_h+=1
            if over_h==h:
                ex = True
                break
        if ex:
            break
    try:
        return h
    except:
        return 0

citations = [0]
print(solution(citations))