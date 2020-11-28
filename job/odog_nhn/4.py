class Solution:
    def solution(self, cardNumber):
        idx = 0 if len(cardNumber) % 2 == 0 else 1
        res = 0

        for i in range(len(cardNumber)):
            if i % 2 == idx:
                if cardNumber[i] >= '5':
                    res += sum(map(int, str(int(cardNumber[i])*2)))
                else:
                    res += int(cardNumber[i])*2
            else:
                res += int(cardNumber[i])
            #print(i, res)
        return "VALID" if res % 10 == 0 else "INVALID"


print(Solution().solution("31378"))
