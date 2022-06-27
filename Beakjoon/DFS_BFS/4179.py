from collections import deque

#문제 조건
''' 
불은 네 방향으로 확산 
미로의 가장자리에서 탈출 가능([x,0],[0,y],[x,c-1],[r-1,y])
벽이 있는 공간은 통과하지 못함
'''

#입력
'''
#: 벽
.: 지나갈 수 있는 공간
J: 지훈이의 미로에서의 초기위치 (지나갈 수 있는 공간)
F: 불이 난 공간
'''
r,c = map(int,input().split()) # row col
arr = [list(input()) for _ in range(r)]
l = [] # 현재 위치
fire = [] # 불의 위치

#풀이
j_q = deque()
f_q = deque()

j_visited = [[0]*c for _ in range(r)]
f_visited = [[0]*c for _ in range(r)]

for x in range(r):
    for y in range(c):
        if arr[x][y] == "J":
            j_q.append((x,y))
            j_visited[x][y] = 1
        elif arr[x][y] == "F":
            f_q.append((x,y))
            f_visited[x][y] = 1

#로직 
def bfs():
    dx = [0,0,1,-1] # 오,왼,아래,위
    dy = [1,-1,0,0]

    while f_q: 
        x,y = f_q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<r and 0<=ny<c: 
                if arr[nx][ny] == "." and f_visited[nx][ny] == 0:
                    f_visited[nx][ny] = f_visited[x][y] + 1
                    f_q.append((nx,ny)) # 이동


    # 시간에 따른 지훈이가 지나간 자리 체크
    while j_q:
        x,y = j_q.popleft()
        
        # 지훈이 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<r and 0<=ny<c: 
                if arr[nx][ny] == "." and j_visited[nx][ny] == 0:
                    if f_visited[nx][ny] == 0 or f_visited[nx][ny] > j_visited[x][y]+1:
                        j_visited[nx][ny] = j_visited[x][y] + 1
                        j_q.append((nx,ny)) # 이동
                        
            else:            
                return j_visited[x][y]   


    return "IMPOSSIBLE"  

#출력
'''
지훈이가 불이 도달하기 전에 미로를 탈출 할 수 없는 경우 IMPOSSIBLE 을 출력한다.
지훈이가 미로를 탈출할 수 있는 경우에는 가장 빠른 탈출시간을 출력한다. 
'''
print(bfs())