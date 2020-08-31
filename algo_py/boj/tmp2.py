'''
문제 설명
숫자가 적혀있는 카드들이 있습니다. 각 숫자가 적힌 카드들은 얼마든지 많이 있다고 가정합니다. 1 이상 10,000 이하의 숫자가 주어졌을 때, 카드를 적절히 선택하여 카드에 적힌 숫자의 합이 주어진 숫자와 같아지도록 하려고 합니다. 예를 들어 숫자 [1, 4, 6]이 적힌 카드가 있을 때 주어진 숫자가 8이라면, 6이 적힌 카드 1장과 1이 적힌 카드 2장을 선택하거나, 4가 적힌 카드 2장을 선택하여 숫자 8을 만들 수 있습니다. 전자는 카드를 3장 사용해야 하며, 후자는 카드를 2장만 사용하면 됩니다. 만들어야 하는 숫자 num과 카드에 적힌 숫자들이 담겨있는 배열 cards가 매개변수로 주어질 때, num을 만드는 데 필요한 카드 개수의 최솟값을 return 하도록 solution 함수를 완성해주세요.

제한사항
num은 1 이상 10,000 이하인 자연수입니다.
cards의 길이는 1 이상 100 이하입니다.
cards의 원소는 1 이상 10,000 이하인 자연수입니다.
cards의 원소는 오름차순으로 정렬되어 주어지며, 중복된 수는 들어있지 않습니다.
cards의 각 숫자가 적힌 카드는 무한히 많다고 가정합니다. 예를 들어 cards가 [2, 3]이라면 2가 적힌 카드와 3이 적힌 카드를 무한히 쓸 수 있습니다.
num을 만들 방법이 존재하지 않는다면 -1을 return 하세요.
'''


def solution(num, cards):
    answer = [10001 for _ in range(num+1)]
    for card in cards:
        if card > num:
            break
        answer[card] = 1
        for i in range(card, num+1):
            answer[i] = min(answer[i-card]+1, answer[i])
    return answer[-1] if answer[-1] < 10001 else -1


num = 15
cards = [1,5,12]
print(solution(num, cards))
