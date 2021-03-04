import io
import os
import sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
def solve():
    sys.stdout.write('\n'.join(map(str, sorted(map(int, (input() for _ in range(int(input()))))))))
if __name__=='__main__':
    solve()
