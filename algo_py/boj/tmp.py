import io
import os
import sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

if __name__ == "__main__":
    n = int(input())
    sys.stdout.write(
        "\n".join(map(str, sorted([int(input()) for _ in range(n)])[::-1])))