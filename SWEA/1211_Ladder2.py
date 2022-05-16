# 0: 아래, 1:왼, 2:오 
dy = [1,0,0]
dx = [0,-1,1]

for _ in range(10):
    test_case = int(input())
    graph = [ [0] + list(map(int,input().split())) + [0] for _ in range(100) ] # 100*100 + 양 옆에 벽 0 추가 -> 102
    distance = 0
    answer = 0

    for i in range(1,101): # 1~100까지 조사 
        count = 0
        x,y = i,0
        if graph[y][x] == 1:
            while 1:
                if y == 99: 
                    break 
                # 왼쪽에 1이 있는 경우
                if graph[y][x-1]: 
                    while 1:
                        y,x = y+dy[1] , x +dx[1] # 왼쪽으로 이동
                        count +=1 
                        if graph[y][x-1] == 0 : # 이제 옆으로 갈 길이없는 경우
                            break 

                #오른쪽에 1이 있는 경우
                elif graph[y][x+1]: 
                    while 1:
                        y,x = y+dy[2] , x +dx[2] # 오른쪽으로 이동
                        count +=1
                        if graph[y][x+1] == 0 : # 갈 길이 없는 경우
                            break
                
                # 없는 경우 = 직진 
                y,x = y+dy[0], x+dx[0]
                count +=1

            if distance: 
                if distance > count : 
                    distance = count 
                    answer = i
            else: # 0인경우 
                distance = count
                answer = i


    print("#{} {}".format(test_case, answer))  # 벽때문    