from collections import deque

def bfs():
    q = deque([n])
    while q:
        x = q.popleft()
        if x == k:
            print(state[x])
            ans = []
            # path에 저장된 경로 값을 통해 거슬러 올라가면서 ans에 저장
            while x != n:
                ans.append(x)
                x = path[x]
            ans.append(n)
            ans.reverse() # 역순으로 저장되어 있으므로 순서를 바꿈
            print(' '.join(map(str,ans)))
            return

        for nx in [x-1,x+1,x*2]:
            if 0 <= nx < MAX and not state[nx]: 
                state[nx] = state[x] + 1
                q.append(nx)
                path[nx] = x #그 전에 지나온 경로를 저장

                
n,k = map(int,input().split())
# n,k = 5, 17
MAX = 100001
state = [0]*MAX
path = [0]*MAX
bfs()


