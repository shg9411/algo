__import__('sys').stdout.write('\n'.join(map(str, sorted(map(int, __import__('sys').stdin.read().splitlines()[1:]), reverse=True))))
