from collections import deque

n = int(input()) 
graph = [list(map(int,input())) for _ in range(n)]
visit = [[False]*n for _ in range(n)]

dx = [0,0,-1,1] # 위 아래 좌 우 
dy = [-1,1,0,0]

def bfs(i,j):
    visit[i][j] = 1
    count = 1 
    que = deque([(i,j)])
    
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx, ny = x + dx[i] , y + dy[i]
            if 0 <= nx < n and 0 <= ny < n: # 범위 내에 있을 때
                if graph[nx][ny] == 1 and not visit[nx][ny]: 
                    visit[nx][ny] = True
                    count +=1 
                    que.append((nx,ny))

    return count 

answer = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visit[i][j]: 
            answer.append(bfs(i,j)) 

print(len(answer))
for i in sorted(answer): 
    print(i)