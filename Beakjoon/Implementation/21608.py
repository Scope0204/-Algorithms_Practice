import sys
input = sys.stdin.readline

# 상 하 좌 우 
dx = [0,0,-1,1]
dy = [1,-1,0,0]

n = int(input())
graph = [[0] * n for _ in range(n)]

likeStu = {} # key : 학생 , val : 좋아하는 학생들
ans = 0 # 만족도

for _ in range(n*n):
    student = list(map(int,input().split()))
    likeStu[student[0]] = student[1:]

    # 좌표 (0,0) 부터 시작해서 알맞은 값을 찾을 것
    max_x = 0
    max_y = 0 
    # 1. 인접한 칸에 있는 좋아하는 학생 수 , 2. 비어있는 인접한 칸
    max_like = -1
    max_empty = -1

    for i in range(n):
        for j in range(n): 
            if graph[i][j] == 0: # 비어있는 칸
                likecnt = 0 # 좋아하는 학생 수 
                emptycnt = 0 # 비어있는 칸의 수 
                for k in range(4): # 주변의 칸 분석(상,하,좌,우)
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0<=nx<n and 0<=ny<n:
                        if graph[nx][ny] in student:  # 좋아하는 학생이 있는지 체크
                            likecnt += 1
                        if graph[nx][ny] == 0: # 비어있는 칸 체크  
                            emptycnt +=1 

                # 조건 1 or 조건 2를 만족한다면 ( 1이 만족한다면 or문은 실행되지 않아 조건 1만 따로 비교할 수 있다 )
                if max_like< likecnt or ( max_like == likecnt and max_empty < emptycnt):
                    # 현재까지 조건에 부합하는 값들로 치환
                    max_x = i
                    max_y = j
                    max_like = likecnt
                    max_empty = emptycnt
                    
    graph[max_x][max_y] = student[0] # 만족하는 위치에 자리를 배치함   


# 학생의 만족도 
# 그 학생과 인접한 칸에 앉은 좋아하는 학생의 수를 구해야 한다. 
for i in range(n):
    for j in range(n):
        cnt= 0 # 만족도 
        like = likeStu[graph[i][j]] # 해당 학생이 좋아하는 학생들  
        for k in range(4): # 인접한 칸 탐색
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < n and 0 <= ny <n: 
                if graph[nx][ny] in like: # 좋아하는 학생이 인접한 칸에 있는 경우
                    cnt += 1

        # 값이 0이면 학생의 만족도는 0, 1이면 1, 2이면 10, 3이면 100, 4이면 1000
        if cnt != 0:
            ans += 10 ** (cnt-1) 

print(ans)

