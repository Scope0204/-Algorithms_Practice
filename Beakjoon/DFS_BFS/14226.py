from collections import deque

def bfs():
    q = deque([n])
    
    while q:
        x = q.popleft()
        if x == k : 
            return state[x]

        for nx in [x-1,x+1,x*2]: 
            if 0 <= nx < 100001 and not state[nx]:
                if nx == x*2 and x != 0 : 
                    state[nx] = state[x]
                    q.appendleft(nx)
                else:
                    state[nx] = state[x] + 1
                    q.append(nx)

n, k = map(int,input().split()) 
state = [0] * 100001  

print(bfs()) 