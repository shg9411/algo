import sys
from collections import Counter

_, m = map(int, input().split())
print('\n'.join((f[0] for f in sorted(Counter(w for w in sys.stdin.read().split() if len(w) >= m).items(), key=lambda x: (-x[1], -len(x[0]), x[0])))))