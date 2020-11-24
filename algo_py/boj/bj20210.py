import re
import sys
input = sys.stdin.readline


def natural_sort(l):
    def convert(text):
        if text.isdigit():
            return (0, int(text), len(text))
        elif text.islower():
            return (1, ord(text)-31.5, text)
        return (1, ord(text), text)

    def separate(key): return [convert(c)
                               for c in re.split('(\d+|.)', key)[1::2]]

    return sorted(l, key=separate)


print('\n'.join(natural_sort([input().rstrip() for _ in range(int(input()))])))