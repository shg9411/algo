h, w = map(int, input().split())
block = list(map(int, input().split()))


def trapping_rain(buildings):
    raindrop = 0
    for i in range(len(buildings)):
        max_left = max(buildings[:i+1])
        max_right = max(buildings[i:])
        which_low = min(max_left, max_right)
        raindrop = raindrop + abs(buildings[i] - which_low)
    return raindrop


print(trapping_rain(block))
