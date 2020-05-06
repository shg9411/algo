import itertools

def solution(baseball):
    for game in baseball:
        game[0] = list(str(game[0]))
    num_list = [str(i) for i in range(1,10)]
    a_l = list(itertools.permutations(num_list,3))
    answer = 0
    for quiz in a_l:
        guess = True
        for game in baseball:
            ball = 0
            strike = 0
            for i in range(3):
                if quiz[i]==game[0][i]:
                    strike+=1
                if quiz[i]==game[0][(i+1)%3]:
                    ball+=1
                if quiz[i]==game[0][(i-1)%3]:
                    ball+=1
            if ball!=game[2] or strike!=game[1]:
                guess = False
                break
        if not guess:
            continue
        answer+=1
    return answer

baseball = [[123,1,1],[356,1,0],[327,2,0],[489,0,1]]
print(solution(baseball))