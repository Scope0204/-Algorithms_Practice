'''
-1 : 블랙홀
0 : 빈공간. 방향 그대로
1~5 : 블록. 블록에 부딛히면 점수 +1 . 이동방향 바뀜
 - 1 : 오->왼 , 위 ->아래 , 왼->위 , 아래->오
 - 2 : 오->왼 , 위 ->오 , 왼->아래 , 아래->위
 - 3 : 오->아래 , 위 ->왼 , 왼->오 , 아래->위
 - 4 : 오->위 , 위->아래, 왼->오, 아래->왼
 - 5 : 오->왼, 위->아래, 왼->오, 아래->위 

6~10 : 웜홀. 같은 번호로 이동. 방향 그대로

게임판 위에서 출발 위치와 진행 방향을 임의로 선정가능 
즉, 모든 위치 + 모든 방향에서 얻을 수 있는 점수의 최대값을 구해라

'''
def wormhole(x,y,graph):
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] == graph[x][y]:
                if i != x or j != y:
                    return i,j
                    

def solution(graph):
    answer =[]
    length = len(graph)
    # 오, 위, 왼, 아래
    # 왼, 아래, 오, 위  (0,-1) (1,0) (0,1) (-1,0) 
    dx = [0,-1,0,1]
    dy = [1,0,-1,0]
    dc = [[],[2,3,1,0],[2,0,3,1],[3,2,0,1],[1,3,0,2],[2,3,0,1]]

    # (i,j) 부터 차례로 계산
    for i in range(length):
        for j in range(length):
            if graph[i][j] == 0: # 빈 공간에서만 실행
                for d in range(4): # 4방향
                    nx,ny= dx[d], dy[d]
                    x,y = i+nx , j+ny 
                    count = 0 
                    # 로직 실행 
                    while 1:
                        if 0<= x < length and 0<= y < length: # 벽안에 있는 경우
                            if graph[x][y] == -1 : # 블랙홀인 경우
                                break

                            elif x == i and y == j : # 다시 돌아온 경우
                                break

                            elif graph[x][y] == 0: # 빈공간인 경우
                                x,y = x+nx,y+ny # 진행 방향으로 이동

                            elif graph[x][y] >= 6 : # 웜홀인 경우 
                                x,y = wormhole(x,y,graph)
                                x,y = x+nx,y+ny

                            else: # 벽에 부딪히는 경우
                                count +=1
                                d = dc[graph[x][y]][d]
                                nx,ny = dx[d], dy[d] # 진행 방향 변경
                                x,y = x+nx, y+ny # 진행 방향으로 이동

                        else: # 벽에 부딪힘
                            count += 1
                            d = dc[5][d] # 방향 전환
                            nx,ny = -nx,-ny
                            x,y = x+nx, y+ny 


                    answer.append(count)
                    
    return max(answer)
                            
t = int(input())
for i in range(t):
    n = int(input())
    graph = [list(map(int,input().split())) for _ in range(n)]
    print("#{} {}".format(i+1,solution(graph)))
    

