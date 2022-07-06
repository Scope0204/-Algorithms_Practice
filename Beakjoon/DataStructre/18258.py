import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
answer = deque()

for _ in range(n):
    c = list(input().split())

    if c[0] == "push":
        answer.append(c[1])
    elif c[0] == "pop":
        print(answer.popleft() if answer else -1)
    elif c[0] == "size":
        print(len(answer))
    elif c[0] == "empty":
        print(0 if answer else 1)
    elif c[0] == "front":
        print(answer[0] if answer else -1)
    elif c[0] == "back":
        print(answer[-1] if answer else -1)

