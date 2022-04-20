import sys
n,k = map(int,sys.stdin.readline().strip().split())
s = list(map(int, sys.stdin.readline().strip().split()))
d = list(map(int, sys.stdin.readline().strip().split()))

for _ in range(k):
    card = [0]*n
    for i in range(n):
        card[d[i]-1] = s[i]
    s = card
    
print(*s)