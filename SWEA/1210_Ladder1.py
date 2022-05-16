# 100 100 크기 
# 풀이방법 : 2인 인덱스를 구해서, 거슬러 올라간다 

for _ in range(10):
    test_case = int(input())
    graph = [ [0] + list(map(int,input().split())) + [0] for _ in range(100)] # 100*100 + 양 옆에 벽 0 추가 -> 102
    x = graph[99].index(2) # 가장 마지막 줄의 x값을 구한다 (x,99)
    y = 99 
    
    # 0: 위, 1:왼, 2:오 
    dy = [-1,0,0]
    dx = [0,-1,1]

    while y != 0:
        # 위로 가고 있을때, 양 옆을 조사한다.

        # #왼쪽에 1이 있는 경우
        if graph[y][x-1]: 
            while 1:
                y,x = y+dy[1] , x +dx[1] # 왼쪽으로 이동
                if graph[y][x-1] == 0 : # 이제 옆으로 갈 길이없는 경우
                    break 

        #오른쪽에 1이 있는 경우
        elif graph[y][x+1]: 
            while 1:
                y,x = y+dy[2] , x +dx[2] # 오른쪽으로 이동
                if graph[y][x+1] == 0 : # 갈 길이 없는 경우
                    break
        
        # 없는 경우 = 직진 
        y,x = y+dy[0], x+dx[0]


    print("#{} {}".format(test_case, x-1))  # 벽때문    