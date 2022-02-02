from collections import deque

n,k = map(int,input().split())
MAX = 100001
state = [-1] * MAX  
cnt = [0] * MAX

q = deque([n])
state[n] = 0
cnt[n] = 1 

while q:
    x = q.popleft()
    #BFS
    for nx in [x-1,x+1,x*2]: 
        if 0 <= nx < MAX:
            if state[nx] == -1:
                state[nx] = state[x] + 1
                cnt[nx] = cnt[x]
                q.append(nx)
            elif state[nx] == state[x]+1:
                cnt[nx]+= cnt[x]

print(state[k])
print(cnt[k])