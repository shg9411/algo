def solution(grades, weights, threshold):
    ts = ["A+","A0","B+","B0","C+","C0","D+","D0","F"]
    tw = [10,9,8,7,6,5,4,3,0]
    score = dict()
    for s,w in zip(ts,tw):
        score[s] = w
    answer = -threshold
    for grade,weight in zip(grades,weights):
        answer+=weight*score[grade]
    
    return answer