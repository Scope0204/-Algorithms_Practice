import sys
input = sys.stdin.readline

n,m = map(int, input().split()) # 파티장크기, 서비스 요청 손님
graph = [ list(map(int, input().split())) for _ in range(n)]


# 플로이드 워셜 알고리즘 수행 -> 그래프 초기화 
for k in range(n):
    for a in range(n):
        for b in range(n):
            # graph[a][b] = min(graph[a][b] , graph[a][k]+graph[k][b])
            if graph[a][b] > graph[a][k]+graph[k][b]:
                graph[a][b] = graph[a][k] + graph[k][b]

for _ in range(m):
    i,j,w = map(int,input().split())

    if graph[i-1][j-1] <= w :
        print("Enjoy other party")
    else:
        print("Stay here")