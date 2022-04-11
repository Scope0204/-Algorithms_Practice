import sys
input = sys.stdin.readline

n = int(input()) # 관찰 횟수 
cow = [[] for i in range(11)]
ans = 0 

for _ in range(n):
    idx,state = map(int,input().split())
    if not cow[idx] or cow[idx][-1] != state:
        cow[idx].append(state)

for arr in cow: 
    if len(arr)>1:
        ans += len(arr)-1

print(ans)