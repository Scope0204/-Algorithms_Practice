import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[0]*n for _ in range(n)]

dx = [0, 1, 0, -1] # 오른쪽, 아래쪽, 왼쪽, 위쪽 순서
dy = [1, 0, -1, 0]

x = n // 2 
y = n // 2 
num = 1 
len = 0  # 특정 방향으로 이동할 길이 얼마나 더할 것인가. for 문으로 동일 작업 수행 가능.

graph[x][y] = num # 시작위치(중간) 1

while 1:
    for i in range(4):
        for _ in range(len):
            x+=dx[i]
            y+=dy[i]
            num+=1
            graph[x][y]=num
            # print('x=',x,'y=',y,'i=',i,'len=',len, '(x,y)=',(dx[i],dy[i]),graph)
            if num==m:  # 찾을 번호의 인덱스 저장
                ans = [x+1, y+1]

    if x==y==0: # 마지막 도착지 (0,0)
        break

    # x,y를 각각 -1씩 해주어, 왼쪽 위로 이동한다. 그 이유는
    # 반복문의 처음 연산은 (0,1)-> 오른쪽으로 이동하여 시작하기 때문에, 그보다 한칸 전에서 시작해서 채우는 것이다
    x -= 1
    y -= 1
    len += 2 # 달팽이 층이 1->3->5->7 순으로 커지기 때문에 +2  


for i in range(n):
    print(*graph[i])
print(*ans)


