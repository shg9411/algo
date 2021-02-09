import io
import os
import sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


def fail(num):
    return abs(num) > 10**9


def div_mod(n, m):
    n, m = m, n
    a = b = 0
    if n < 0:
        a = 1
        n = -n
    if m < 0:
        b = 1
        m = -m
    div, mod = divmod(n, m)
    if a:
        mod = -mod
    if a ^ b:
        div = -div
    return div, mod


def solve():
    def gostack(n, cmd):
        st = [n]
        for line in cmd:
            if line[:3] == "NUM":st.append(int(line[4:]))
            elif not st:return
            elif line == "POP":st.pop()
            elif line == "INV":st.append(-st.pop())
            elif line == "DUP":st.append(st[-1])
            elif len(st) == 1:return
            elif line == "SWP":
                v2,v1 = st.pop(),st.pop()
                st.append(v2)
                st.append(v1)
            elif line == "ADD":
                v = st.pop()+st.pop()
                if fail(v):return
                else:st.append(v)
            elif line == "SUB":
                v = -st.pop()+st.pop()
                if fail(v):return
                else:st.append(v)
            elif line == "MUL":
                v = st.pop()*st.pop()
                if fail(v):return
                else:st.append(v)
            elif st[-1] == 0:return
            elif line == "DIV":st.append(div_mod(st.pop(), st.pop())[0])
            elif line == "MOD":st.append(div_mod(st.pop(), st.pop())[1])
        return st
    r = []
    while 1:
        cmd = []
        while 1:
            c = input().decode().strip()
            if c == "END":break
            if c == "QUIT":return r
            cmd.append(c)
        for _ in range(int(input())):
            res = gostack(int(input()), cmd)
            if res and len(res) == 1:r.append(res[-1])
            else:r.append("ERROR")
        r.append('')
        input()


if __name__ == "__main__":
    print('\n'.join(map(str, solve())))