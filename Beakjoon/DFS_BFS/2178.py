# 틀린 코드 : dfs 로 풀이시도 
# def dfs(x,y,c):
#     cnt = c+1
#     if count[x][y] == 0 or count[x][y] > cnt:
#         count[x][y] = cnt

#         if x == n-1 and y == m-1:
#             return

#         for i in range(4):
#             nx = x+dx[i]
#             ny = y+dy[i]

#             if 0 <= nx < n and 0 <= ny < m:
#                 if graph[nx][ny] == 1: # 갈 수 있는경우
#                     dfs(nx,ny,cnt)

#     else:
#         return 
   
# n,m = map(int,input().split()) 
# graph = [list(map(int,input())) for _ in range(n)]
# count = [[0]*m for _ in range(n)]
# dx = [0,0,-1,1]
# dy = [1,-1,0,0]

# dfs(0,0,0)
# print(count[n-1][m-1])

from collections import deque

def bfs(x,y):
    queue = deque([(x,y,1)])
    visited[x][y] == True

    while queue:
        x,y,count = queue.popleft()
        if x == n-1 and y == m-1:
            return print(count)

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and not visited[nx][ny]: # 갈 수 있는경우
                    queue.append((nx,ny,count+1))
                    visited[nx][ny] = True
    
    

n,m = map(int,input().split()) 
graph = [list(map(int,input())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
bfs(0,0)
