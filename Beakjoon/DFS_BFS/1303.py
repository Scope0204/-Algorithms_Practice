from collections import deque

def bfs(x,y,color):
    count = 1
    que = deque([(x,y)])
    visited[x][y] = True

    while que: 
        x,y = que.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<= nx < m and 0 <= ny < n:
                if graph[nx][ny] == color and not visited[nx][ny]:
                    visited[nx][ny] = True
                    que.append((nx,ny))
                    count += 1 

    return count 

# 상 하 좌 우 
dx = [0,0,-1,1]
dy = [1,-1,0,0]
n,m = map(int,input().split())
graph = [list(input()) for _ in range(m)] 
visited = [[False] * n for _ in range(m)]

white, blue = 0,0

for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            if graph[i][j] == "W":
                white += bfs(i,j,"W")**2  
            elif graph[i][j] == "B": 
                blue += bfs(i,j,"B")**2

print(white, blue)