t = int(input())

def dfs(n,c):
    global answer
   
    visited[n] = True
    if answer < c :
        answer =c
    
    for i in graph[n]:
        if not visited[i]: 
            dfs(i,c+1)
            visited[i] = False

for test_case in range(1,t+1):
    n,m = map(int,input().split()) # n개의 노드 , m개의 줄(간선)
    graph = [[]*(n+1) for _ in range(n+1)]
   
    for i in range(m):
        x,y = map(int,input().split())
        graph[x].append(y)
        graph[y].append(x)
        
    answer = 0
    for j in range(1,n+1):
        visited = [False for _ in range(n+1)]
        dfs(j,1)
        
    
    print("#{} {}".format(test_case, answer))
    
