import sys


def work():
    a = int(input())
    list_index = []
    list_stack = []
    list_show = []
    f = 0
    r = 0

    for i in range(0, a):
        y = str(sys.stdin.readline())
        ant = y.rstrip()
        list_index.append(ant)

    index = 0
    while 1:
        if 'push' in list_index[index]:  # 명령에 push 가 있으면
            list_stack.append((list_index[index]).split(" ")[1])
            r += 1

            index += 1
        elif 'front' in list_index[index]:
            if not list_stack:
                list_show.append(-1)
                index += 1
            else:
                list_show.append(int(list_stack[f]))
                index += 1
        elif list_index[index] == "back":
            if len(list_stack) != 0:
                list_show.append(int(list_stack[-1]))
                index += 1
            else:
                list_show.append(-1)
                index += 1
        elif list_index[index] == "size":
            if f + 1 > r:
                list_show.append(0)
                index += 1
            else:
                list_show.append(len(list_stack))
                index += 1
        elif list_index[index] == "empty":
            if f + 1 > r:
                list_show.append(1)
                index += 1
            else:
                list_show.append(0)
                index += 1
        elif list_index[index] == "pop":
            if f + 1 <= r:
                list_show.append(int(list_stack[f]))
                f += 1
                index += 1
            elif f + 1 > r:
                list_show.append(-1)
                index += 1
        else:
            pass

        if index == a:
            for i in list_show:
                print(i)
            quit()

    quit()


work()
