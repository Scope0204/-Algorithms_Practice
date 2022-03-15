def dfs(n):
    print(n, end=' ') # 지나온(방문한) 순서대로 기록
    visited[n] = True # 방문한 곳을 체크 
    for i in graph[n]: 
        if not visited[i]: # 이어져있으나 지금껏 방문하지 않은 곳
            dfs(i)  

def bfs(n):
    visited[n]= True
    queue = deque([n])
    while queue: 
        num = queue.popleft() 
        print(num, end=' ') 
        for i in graph[num]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                


from collections import deque
n,m,v = list(map(int,input().split())) # n: 정점의 개수, m: 간선의 개수, v: 탐색을 시작하는 번호 
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 갈 수 있는 경로 정렬 -> 낮은 번호를 우선적으로 감 
for i in range(1,n+1):
    graph[i].sort()

dfs(v)
print()
visited = [False] * (n+1) # 초기화
bfs(v)

