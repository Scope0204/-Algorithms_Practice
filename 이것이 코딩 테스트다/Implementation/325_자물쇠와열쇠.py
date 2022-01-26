# 2차원 리스트 90도 회전
def rotate_matrix_by_90_degree(a):
    n = len(a)
    m = len(a[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n):
         for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result

# 자물쇠가 열리는지 체크 
def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length *2):
        for j in range(lock_length, lock_length *2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key,lock):
    n = len(lock)
    m = len(key)
    # 자물쇠의 크기를 기존의 3배로 변환
    new_lock = [[0] * (n*3) for _ in range(n*3)]
    # 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]

    # 4가지 방향에 대해서 확인
    for rotation in range(4):
        key = rotate_matrix_by_90_degree(key) # rotation = 0(90) , 1(180) , 2(270) , 3(360)
        for x in range(n*2):
            for y in range(n*2):
                # 자물쇠에 열쇠 끼워 넣기 
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                        # print("i는", i , "j는", j , "x는", x+i , "y는", y+j, "현재", new_lock[x+i][y+j] )
                       

                # 새로운 자물쇠에 열쇠가 정확히 들어맞는지 검사
                if check(new_lock) == True:
                    print(rotation) # 0. 90도의 경우에서 검사햇음. 
                    return True
                # 자물쇠에서 열쇠를 다시 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
                        
    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))