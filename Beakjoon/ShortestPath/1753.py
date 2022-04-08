import sys, heapq

input = sys.stdin.readline
INF = sys.maxsize

V,E = map(int,input().split()) # 정점의 개수, 간선의 개수
k = int(input()) # 시작 노드
graph = [[] for _ in range(V+1)] # index 0 = v , index 1 = w
distance = [INF]*(V+1) # 최단 거리 

# u -> v , 가중치: w 
for i in range(E):
    u,v,w = map(int,input().split())
    graph[u].append((v,w)) # index 0 = v , index 1 = w

def dijkstra(start):
    q = [] 
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q) # 가장 최단 거리가 짧은 노드에 대한 정보 
        # 이미 처리된 노드라면 무시
        if distance[now] < dist: 
            continue

        # 현재 노드와 연결된 다른 인접한 노드들 확인
        for i in graph[now]:
            cost = dist + i[1] # 해당 노드 거리 = 현재 노드 거리 + 가중치
            if cost < distance[i[0]]: # 현재 노드에서 가는 거리가 더 가까울 경우
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0])) 

dijkstra(k) # 출발 위치에서 다익스트라 알고리즘 수행


for i in range(1,V+1):
    if distance[i] == INF:
        print("INF")
    else: 
        print(distance[i])