import sys
tree = dict()
i = 0
for t in sys.stdin:
    i += 1
    t = t.rstrip()
    try:
        tree[t] += 1
    except:
        tree[t] = 1

tmp = sorted(tree.items())

for t in tmp:
    print('%s %.4f' % (t[0], t[1]/i*100))
