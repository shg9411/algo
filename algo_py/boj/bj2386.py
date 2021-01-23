import sys
for x in sys.stdin:
    if x=='#\n':
        break
    print("%c %s" % (x[0], x[2:].lower().count(x[0])))
