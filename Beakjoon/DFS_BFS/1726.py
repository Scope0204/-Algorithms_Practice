'''
# 문제
로봇은 바라보는 방향으로 움직이며, 동서남북 중 하나이다.
0은 갈 수 있으며 1은 갈 수 없다.
로봇의 현재 위치와 바라보는 방향이 주어질때,
로봇을 원하는 위치로 이동시키고, 원하는 방향으로 바라보도록 하려면 
최소 몇번의 명령이 필요할까

# 로봇 제어 명령어 
1. go k: 현재 향하고 있는 방향으로 k칸 만큼 움직임 
2. trun dir: dir는 왼쪽또는 오른쪽이며, 90도로 회전한다
'''
from collections import deque

# 로직
def bfs(m,n,k):
    global M,N

    q = deque([(m,n,k)])

    while q:
        x,y,k = q.popleft()

        for nk in range(1,5):
            nx,ny = x+dir[nk][0] , y+dir[nk][1]
        
            if 0<=nx<M and 0<=ny<N and not visited[nx][ny] and graph[nx][ny] == 0 :
                if nk == k:
                    if visited[x][y] == 0: #처음부터 방향이 맞을 때
                        visited[x][y] = 1
                    visited[nx][ny] = visited[x][y]
                else: 
                    if (k == 1 and nk == 2) or (k == 2 and nk == 1) or (k == 3 and nk == 4) or (k == 4 and nk == 3):
                        visited[nx][ny] = visited[x][y]+3
                    else:
                        visited[nx][ny] = visited[x][y]+2
                
                q.append((nx,ny,nk))

                if nx == em-1 and ny == en-1 :
                    return nk



# 입력
M,N = map(int,input().split()) # 세로, 가로
graph = [ list(map(int,input().split())) for _ in range(M)]
m,n,k = map(int,input().split()) #출발지점 x y, 바라보는 방향 k 
em,en,ek = map(int,input().split()) # 도착지점 x y, 바라보는 방향

# 풀이
dir=[(0,0),(0,1),(0,-1),(1,0),(-1,0)] #방향 : 1,2,3,4 : 동,서,남,북 : 오 왼 아 위
visited = [[0]*N for _ in range(M)]

# 출력 : 최소 명령 횟수
lk = bfs(m-1,n-1,k)
if ek == lk: # 마지막 바라보는 곳과 같다면
    print(visited[em-1][en-1])
else:
    if (ek == 1 and lk == 2) or (ek == 2 and lk == 1) or (ek == 3 and lk == 4) or (ek == 4 and lk == 3):
        print(visited[em-1][en-1]+2)
    else:
        print(visited[em-1][en-1]+1)

