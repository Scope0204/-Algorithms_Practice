from collections import deque

def bfs(n,k):
    que = deque([n])

    while que:
        x = que.popleft()
        if x == k: 
            return visited[k]

        for nx in [x-1,x+1,x*2]:
            if 0<=nx< 100001 and not visited[nx]:
                if nx == x*2 and x != 0:
                    visited[nx] = visited[x]
                    que.appendleft(nx) # 주의 
                else:
                    visited[nx] = visited[x]+1
                    que.append(nx)


n,k = map(int, input().split())
visited = [0]*100001
print(bfs(n,k))

