for _ in range(10):
    t = int(input())
    graph = [ list(map(int,input().split())) for _ in range(100)]

    # 행,열,오른쪽대각, 왼쪽대각 의 합들의 모임
    answer = []
    
    dia_sum1 = 0 # 오른 대각
    dia_sum2 = 0 # 왼 대각

    for i in range(100):
        dia_sum1 += graph[i][i]
        dia_sum2 += graph[i][99-i]

        row_sum = 0
        col_sum = 0 
        for j in range(100):
            # (i,0) ~ (i,99) -> row 
            row_sum += graph[i][j]  
            # (0,i) ~ (99,i) -> col
            col_sum += graph[j][i]

        answer.append(row_sum)
        answer.append(col_sum)
        
    answer.append(dia_sum1)
    answer.append(dia_sum2)

    print("#{} {}".format(t,max(answer)))