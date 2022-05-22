# 정답 코드 : stack
T = 10
for tc in range(1, T+1):
    N = int(input())
    a = [list(map(int, input().split())) for _ in range(N)]
    # 1: N극 성질-> 빨강이  2: S극 성질-> 파랭이

    cnt = 0
    for j in range(N):  # (0,j) 열탐색
        r, c = 0, j
        stack = []
        # 아래로 내려가면서 <1--2> 의 순서이면 체킹
        while r < N:
            if not stack and a[r][c] == 1:  # 스택이 비어있는 상태이면서 1 이면 stack에 넣음
                stack.append(1)
            elif stack and a[r][c] == 2:  # 스택에 1이 있는 상태에서 2가 나오면 pop 해서 cnt에 더해주기
                cnt += stack.pop()
            r += 1  # 아래로 진행하기 위해 row 인덱스 증가시켜주기

    print("#{} {}".format(tc, cnt))