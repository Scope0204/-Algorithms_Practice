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
graph = [ list(map(int,input().split())) for _ in range(n)]
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

