def dfs(num):
    visited[num] = True
    for i in graph[num]:
        if not visited[i]: # False인 경우
            global ans
            ans += 1 
            dfs(i) 

n = int(input()) # 컴퓨터의 수 
conn = int(input()) # 연결된 쌍의 수 
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
ans = 0 

for _ in range(conn):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1) # 2,5

print(ans)
 