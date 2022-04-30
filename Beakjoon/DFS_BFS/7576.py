import sys
from collections import deque

sys = sys.stdin.readline

m,n = map(int,input().split())
graph = [list(map(int,input().strip().split())) for _ in range(n)]

dx = [0,0,-1,1] # 위 아래 좌 우 
dy = [-1,1,0,0]

que = deque([])

for i in range(n): 
    for j in range(m):
        if graph[i][j] == 1: 
            que.append([i,j]) 

def bfs():
    while que:
        x,y= que.popleft()

        for i in range(4):
            nx = x + dx[i] 
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0: 
                graph[nx][ny] = graph[x][y] + 1
                que.append((nx,ny))

bfs()

answer = 0 
no = 0 
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0: 
            no = 1
            print(-1)
            break
        else:
            if answer < graph[i][j]: 
                answer = graph[i][j]
    if no: 
        break

if not no:
    print(answer-1)