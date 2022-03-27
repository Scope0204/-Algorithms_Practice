from collections import deque

def bfs(n,k):
    que = deque([n])

    while que: 
        x = que.popleft()
        if x == k: 
            break

        for nx in [x-1,x+1,x*2]:
            if 0 <= nx < 100001:
                if visited[nx] == -1 : 
                    visited[nx] = visited[x]+1
                    count[nx] = count[x]
                    que.append(nx)
                elif visited[nx] == visited[x]+1:
                    count[nx] += count[x] 
                    


n,k = map(int,input().split())

visited = [-1] * 100001
count = [0] * 100001
visited[n] = 0
count[n] = 1 
bfs(n,k)

print(visited[k])
print(count[k])
