from collections import deque

def bfs(x,y):
    size = 1
    visited[x][y] = True
    que = deque([(x,y)])

    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0<= ny <m:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    que.append((nx,ny))
                    visited[nx][ny] = True
                    size += 1

    return size

    

n,m,k = map(int,input().split()) # 세로, 가로, 음식물쓰레기 개수 
graph = [[0]*m for _ in range(n)]
visited = [[False]*m for _ in range(n)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]

for _ in range(k):
    i,j = map(int,input().split())
    graph[i-1][j-1] = 1 # 쓰레기가 있는 곳에 값 추가

ans = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            size = bfs(i,j)
            if ans < size:
                ans = size
            

print(ans)
       
