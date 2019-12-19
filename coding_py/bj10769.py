import sys

line = sys.stdin.readline()
good = line.count(':-)')
bad = line.count(':-(')

if good+bad == 0:
    print('none')
elif good == bad:
    print('unsure')
elif good > bad:
    print('happy')
else:
    print('sad')
