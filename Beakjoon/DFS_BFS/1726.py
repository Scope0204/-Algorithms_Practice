'''
# 문제
로봇은 바라보는 방향으로 움직이며, 동서남북 중 하나이다.
0은 갈 수 있으며 1은 갈 수 없다.
로봇의 현재 위치와 바라보는 방향이 주어질때,
로봇을 원하는 위치로 이동시키고, 원하는 방향으로 바라보도록 하려면 
최소 몇번의 명령이 필요할까

# 로봇 제어 명령어 
1. go k: 현재 향하고 있는 방향으로 k칸 만큼 움직임 (최소 1 ~ 최대 3)
2. trun dir: dir는 왼쪽또는 오른쪽이며, 90도로 회전한다
'''
from collections import deque

#방향 : idx 0,1,2,3: 동,서,남,북
dx = [0,0,1,-1]
dy = [1,-1,0,0]

# 로직
def bfs():
    q = deque([(sm-1,sn-1,sd-1,0)]) 
    visited = [[[0]*4 for _ in range(N)] for _ in range(M)] # 동서남북에따라 방문기록을 남김
    visited[sm-1][sn-1][sd-1] = 1 # 시작 위치 

    while q: 
        # print(q)
        x,y,d,count = q.popleft()
        if (x,y,d) == (em-1,en-1,ed-1): # 마지막 조건과 위치와 이동방향이 같은 경우
            return count

        #1. go k 1~3 
        for k in range(1,4):
            nx,ny,nd = x+dx[d]*k,y+dy[d]*k,d # 방향은 그대로
            if 0<=nx<M and 0<=ny<N and graph[nx][ny] == 0:
                if not visited[nx][ny][nd]:
                    visited[nx][ny][nd] = 1
                    q.append((nx,ny,nd,count+1))
            else: # 벽 밖으로 나가거나 1을 만나면 stop
                break
            
                
        #2. turn dir 90도로 방향 바꾸기. 180도 회전시 2회 소모 
        for nd in range(4):
            if nd != d and not visited[x][y][nd]:
                visited[x][y][nd] = 1
                if (d == 0 and nd == 1) or (d == 1 and nd == 0) or (d == 2 and nd == 3) or (d == 3 and nd == 2):
                    q.append((x,y,nd,count+2))
                else:
                    q.append((x,y,nd,count+1))
# 입력
M,N = map(int,input().split()) # 세로, 가로
graph = [ list(map(int,input().split())) for _ in range(M)]
sm,sn,sd = map(int,input().split()) #출발지점 x y, 바라보는 방향 d
em,en,ed = map(int,input().split()) # 도착지점 x y, 바라보는 방향

print(bfs())