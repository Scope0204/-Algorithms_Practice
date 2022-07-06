from collections import deque

n = int(input())
d = deque(enumerate(map(int, input().split())))
ans = [] 
while d:
    idx, balloon = d.popleft()
    ans.append(idx+1)

    if balloon > 0:
        d.rotate(-(balloon-1))
    elif balloon < 0:
        d.rotate(-balloon)

print(' '.join(map(str,ans)))
