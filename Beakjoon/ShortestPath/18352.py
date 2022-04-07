# 1. 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
# 2. A번 도시에서 B도시로 이동하는 단방향 도로 -> M개
# 출력 : X로부터 출발하여 도달할 수 있는 도시 중 최단거리가 K인 것을 오름차순 출력, 하나도 없으면 -1

from collections import deque
import sys
input = sys.stdin.readline

n,m,k,x = map(int,input().split())

graph = [[] for _ in range(n+1)]
distance = [ 1e9 for _ in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

distance[x] = 0
q = deque([x])

while q:
    node = q.popleft()

    for next_node in graph[node]:
        if distance[node]+1 < distance[next_node]: 
            distance[next_node] = distance[node]+1 
            q.append(next_node)

if k not in distance:
    print(-1)
else:
    for i in range(len(distance)):
        if distance[i] == k:
            print(i)
