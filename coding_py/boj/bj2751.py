import sys
sys.stdout.write(
    '\n'.join(map(str, sorted(map(int, sys.stdin.read().splitlines()[1:])))))
