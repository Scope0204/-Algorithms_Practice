from collections import deque
'''
# 1. 1년 후 빙산 높이
def next_year():
    global graph,n,m

    new_graph = [[0]*m for _ in range(n)]
    dx = [0,0,1,-1] # 동서남북 - 오,왼,아래,위
    dy = [1,-1,0,0]

    for x in range(n):
        for y in range(m):
            if graph[x][y]: # 0이 아닌경우 
                new_graph[x][y] = graph[x][y]
                for i in range(4):
                    nx = x+dx[i]
                    ny = y+dy[i]
                    if nx >= 0 and ny >= 0: #동서남북의 인덱스가 그래프에 있을떄
                        if not graph[nx][ny]: # 0인경우
                            if new_graph[x][y]: # 0이 아니라면 높이 -1
                                new_graph[x][y] -= 1
    graph = new_graph # 그래프 최신화

# 2. 빙산 덩어리 갯수 
def next_ice():
    global graph,n,m,iceberg

    iceberg = 0
    visited = [[False]*m for _ in range(n)]
    
    for x in range(n):
        for y in range(m):
            if not visited[x][y]:
                visited[x][y] = True
                if graph[x][y]:
                    dfs(x,y,visited)
                    iceberg += 1

    return iceberg

#3. 찾기 DFS
def dfs(x,y,visited):
    global graph,n,m
    
    dx = [0,0,1,-1] # 동서남북 - 오,왼,아래,위
    dy = [1,-1,0,0]

    for i in range(4): 
        nx = x+dx[i]
        ny = y+dy[i]
        if nx >= 0 and ny >= 0 and not visited[nx][ny]: #동서남북의 인덱스가 그래프에 있을떄
            visited[nx][ny] = True
            if graph[nx][ny]: # 값이 있는 경우 = 이어진 하나의 빙산
                dfs(nx,ny,visited) # 해당 위치에서 동서남북 체크

n,m = map(int,input().split()) #행,열
graph = [list(map(int,input().split())) for _ in range(n)]
iceberg = 1 # 처음 빙산의 갯수는 항상 1 
answer = 0

while iceberg<2:
    if iceberg == 0:
        answer = 0
        break
    answer += 1
    next_year() # 다음 해 빙산의 높이
    next_ice() # 빙산 갯수 측정

print(answer)
'''

#로직 
def bfs():
    q = deque()
    q.append(iceberg[0])
    select_iceberg = 0 # 조회한 빙산의 갯수
    dx = [0,0,1,-1] # 동서남북 - 오,왼,아래,위
    dy = [1,-1,0,0]
    melting=[] # 1년후, 녹을 빙산의 좌표값과 녹는 높이


    visited = [[False]*m for _ in range(n)]
    visited[iceberg[0][0]][iceberg[0][1]] = True # 시작점 빙산

    while q:
        x,y = q.popleft()

        select_iceberg += 1  
        count = 0 # 녹는 높이

        # 1. 주변 바다 탐색(0인 값)
        for i in range(4):
            nx = dx[i]+x
            ny = dy[i]+y
            if nx >= 0 and ny >= 0:
                if graph[nx][ny] == 0: #주변이 바다 -> 갯수만큼 녹음
                    count += 1
                elif graph[nx][ny] and not visited[nx][ny]: #빙산인 경우 and 아직 방문하지않음
                    visited[nx][ny] = True
                    q.append((nx,ny))
        
        if count != 0 : # 녹는 빙산이라면(= 주변에 바다가 있다면)
            melting.append((x,y,count)) # 해당 빙산의 좌표와 녹는점 

    #2. 0의 갯수만큼 빙산이 녹음(단, 0인경우 더 이상 녹지 않는다)
    for x,y,cnt in melting:
        graph[x][y] = graph[x][y] - cnt if graph[x][y]-cnt > 0 else 0  
        
        #다 녹은 빙산은  bfs 체크리스트에서 제외 
        if graph[x][y] == 0 and (x,y) in iceberg: 
            iceberg.remove((x,y)) 
        
    # 조회한 빙산의 갯수
    return select_iceberg


#입력
n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

#풀이
year = 0
iceberg = []

for x in range(n):
    for y in range(m):
        if graph[x][y]:
            iceberg.append((x,y)) # 빙산이 있는 위치 값 추가

while 1:
    # 선택된 빙산의 갯수가 현재 빙산의 갯수와 다르다 -> 쪼개졌다 
    if len(iceberg) == 0 : 
        year = 0 
        break
    
    if len(iceberg) != bfs():
        break

    year += 1

    # # 전부 다 녹은 경우 = 그래프의 모든 값의 합이 0인 경우 
    # if sum(map(sum, graph[1:-1])) == 0: 
    #     year = 0
    #     break

#출력
print(year)