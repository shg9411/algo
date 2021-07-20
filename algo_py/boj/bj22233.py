import sys


n, _ = map(int, input().split())
inputs = sys.stdin.read().split()
keywords = set(inputs[:n])
blogs = inputs[n:]
for blog in blogs:
    words = set(blog.split(','))
    keywords -= words
    print(len(keywords))