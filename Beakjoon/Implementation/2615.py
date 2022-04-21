graph = [list(map(int,input().split())) for _ in range(19)] 

dx = [-1,0,1,1] # 오위 오 오른아래 하
dy = [1,1,1,0]

find = 0 

# 2개 이후 해당 방향에서 3개 더 같은 바둑돌이 나온다면 ok. 3개를 넘으면 안됨
def check2(x,y,i):
    count = 0 # count가 3개여야 ok 

    nx = x+dx[i]
    ny = y+dy[i]

    while 1:
        if 0 <= nx < 19 and 0 <= ny < 19: 
            if graph[nx][ny] == graph[x][y]: # 연속해서 같은 바둑돌을 만났을 때
                count += 1
                nx = nx + dx[i]
                ny = ny + dy[i]
            else:
                break 
        else: 
            break

    return count

def check(x,y):
    temp = False
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0 <= nx < 19 and 0 <= ny < 19: # 범위 안에 속하는지
            if graph[nx][ny] == graph[x][y]: # 연속해서 같은 바둑돌을 만났을 때
                # 이 시점에서 연속한 바둑돌은 2개이다
                # 이후에 연속해서 3개가 더 같은 경우 오목 조건 완성
                if check2(nx,ny,i) == 3 : # 정방향에서는 오목인지 확인이되었다
                    # 이제 그 칸의 한칸 뒤가 같은지 살펴본다. 같다면 육목 이상이기 때문에 오답! 달라야 오목이다
                    nx = x - dx[i] 
                    ny = y - dy[i] 
                    if 0 > nx and 0 > ny : # 만약 뒤가 0보다 작다  = 오목
                        temp = True
                        break
                    else: 
                        if graph[nx][ny] != graph[x][y]: # 다르면 오목이다
                            temp = True
                            break

    return temp

for i in range(19):
    for j in range(19):
        if graph[i][j] != 0: # 바둑알인 경우 체크 
            if check(i,j): # 리턴 값이 있다 == 승리했다 
                find = 1
                print(graph[i][j])
                print(i+1,j+1)
                break
    if find: 
        break

if not find: 
    print(0)