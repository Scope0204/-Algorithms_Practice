from collections import deque

# 로직
def bfs(a,b):

    q = deque([(a,b)])
    size = 0 
    while q:
        x,y = q.popleft()
        size +=1 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m : 
                if arr[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = key # 속하는 그룹의 key값을 넣어준다 
                    q.append((nx,ny))

    return size



# 입력
n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)] # 0 또는 1이 들어있다

# 풀이 
visited = [[0]*m for _ in range(n)]

dx = [0,0,1,-1] # 오,왼,아래,위
dy = [1,-1,0,0]

group = {} 
key = 1
answer = 0

# 그룹화
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and not visited[i][j]:
            visited[i][j] = key
            size = bfs(i,j)
            group[key] = size # {key:size}
            key += 1 

for x in range(n):
    for y in range(m):
        if arr[x][y] == 0: 
            s = set()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if arr[nx][ny] == 1:
                        s.add(visited[nx][ny])

            ans = 1 # 0을 1로 바꿧으니 추가

            for k in s:
                ans += group[k]

            if answer < ans:
                answer = ans

print(answer)