# L : 왼쪽 한칸 이동 . R : 오른쪽 . U: 위 . D : 아래
n = int(input())
plans = input().split()
x,y = 1,1
dx = [0,0,-1,1]
dy = [-1,1,0,0]
moving = ['L','R','U','D']

# 이동 계획 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기 
    for i in range(len(moving)):
        if plan == moving[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        # 공간을 벗어나면 무시
    if nx < 1 or ny <1 or nx > n or ny > n:
        continue
    x,y = nx,ny

print(x,y)