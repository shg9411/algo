import sys

def perfect(c):
    t = ['[', ']', '(', ')']
    if c in t:
        return True
    else:
        return False

while True:
    readt=sys.stdin.readline().rstrip()
    if readt==".":
        break
    toparse=(''.join(filter(perfect, readt))).replace('()', '(1,)').replace(')(', '),(').replace('][', '],[').replace(')[', '),[').replace('](', '],(')
    print(toparse)
    try:
        if toparse.startswith("]"):
            print("no")
        else:
            eval("["+toparse+"]")
            print("yes")
    except:
        print("no")
