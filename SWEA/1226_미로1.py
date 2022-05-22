t = 10
for _ in range(t):
    n = int(input())
    graph = [ list(map(int,input())) for _ in range(16)] # 16*16
    
    # 위,아래,오,왼
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]

    stack = []
    temp = False

    # 시작 지점 찾기 
    for i in range(16):
        for j in range(16):
            if graph[i][j] == 2:
                stack.append([i,j])
                temp = True
                break
        if temp:
            break
        
    answer = 0 
    while stack:
        x,y = stack.pop(0)
        for i in range(4):
            nx = x + dx[i] 
            ny = y + dy[i]

            if 0<=nx<16 and 0<=ny<16 :
                if graph[nx][ny] == 3:
                    answer = 1
                    break # for문 탈출
                elif graph[nx][ny] ==0 : # 0인경우
                    graph[nx][ny] = 1
                    stack.append([nx,ny])

        if answer: # 도달 한 경우
            break 

    print("#{} {}".format(n,answer))
