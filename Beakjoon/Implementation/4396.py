import sys
input = sys.stdin.readline

n = int(input())
graph = [ list(input().strip()) for _ in range(n)] 
user_input = [ list(input().strip()) for _ in range(n)]
ans=[['.']*n for _ in range(n)]
boom_cnt = 0 

'''
0,0  0,1  0,2
1,0 (1,1) 1,2
2,0  2,1  2,2 
'''
dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

def check(x,y):
    count = 0
    for i in range(8): 
        nx = x+dx[i]
        ny = y+dy[i]

        if 0<=nx<n and 0<=ny<n:
            # print(x,y,graph[nx][ny])
            if graph[nx][ny] == '*': # 지뢰가 있다면 
                count+=1 
    
    return str(count)


for i in range(n):
    for j in range(n):
        if user_input[i][j] == 'x':
            if graph[i][j] == '*': # 밟은 곳이 폭탄인 경우
                ans[i][j] = '*'
                boom_cnt += 1
            else:
                ans[i][j] = check(i,j)

if boom_cnt: # 지뢰를 밟았다면, 지뢰가 있는 땅은 표시해줘야 함
    for i in range(n):
        for j in range(n):
            if graph[i][j] == '*':
                ans[i][j] = '*'

for i in range(n):
    print(''.join(ans[i]))