# 0은 빈방 1은 벽 
# (1, 1)과 (N, M)은 항상 뚫려있다 -> mapp[0][0] = 0 , mapp[n-1][m-1] = 0
# (x+1, y), (x, y+1), (x-1, y), (x, y-1) 

from collections import deque

n,m = map(int,input().split()) # (m,n)
mapp = []
for i in range(m):
    mapp.append(list(map(int,input())))  
attack= [[0]*n for _ in range(m)]
visited = [[0]*n for _ in range(m)]

q = deque([[0,0]])
visited[0][0] = 1
while q: 
    x,y = q.popleft()
    if x == m-1 and y == n-1: 
        print(attack[x][y])
        break
    
    for nx, ny in [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]:
        if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
            visited[nx][ny] =1

            if mapp[nx][ny] == 0: # 벽이 없는 경우 
                attack[nx][ny] = attack[x][y]
                q.appendleft([nx,ny])
            else:
                attack[nx][ny] = attack[x][y] + 1
                q.append([nx,ny])





