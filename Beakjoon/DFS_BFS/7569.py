import sys
from collections import deque

input = sys.stdin.readline

M,N,H = map(int,input().split()) # 가로, 세로, 상자 수 
boxes = [[] for _ in range(H)]

# 위 아래 좌 우 + 앞,뒤
dx = [0,0,-1,1,0,0] 
dy = [-1,1,0,0,0,0]
dh = [0,0,0,0,1,-1]

for i in range(H):
    boxes[i] = [list(map(int,input().strip().split())) for _ in range(N)] 

que = deque([])
for h in range(H):
    for n in range(N):
        for m in range(M):
            if boxes[h][n][m] == 1:  
                que.append([h,n,m])

def bfs():
    while que:
        h,x,y = que.popleft()

        for i in range(6):
            nx,ny,nh = x+dx[i] , y+dy[i] , h+dh[i]
            if 0<=nx<N and 0<=ny<M and 0<=nh<H:
                if boxes[nh][nx][ny] == 0:
                    boxes[nh][nx][ny] = boxes[h][x][y] + 1
                    que.append((nh,nx,ny))
bfs()

answer = 0 
no = 0 
for h in range(H):
    for i in range(N):
        for j in range(M):
            if boxes[h][i][j] == 0: 
                no = 1
                print(-1)
                break
            else:
                if answer < boxes[h][i][j]: 
                    answer = boxes[h][i][j]
        if no: 
            break
    if no:
        break

if not no:
    print(answer-1)

