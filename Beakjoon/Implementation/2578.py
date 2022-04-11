from itertools import count
import sys
input = sys.stdin.readline

def check():
    ans = 0
    # 가로 빙고
    for i in range(5):
        count1 = 0 
        for j in range(5):
            if visited[i][j]:
                count1 += 1
                if count1 == 5:
                    ans +=1 
            else:
                break

    # 세로 빙고 체크 
    for j in range(5):
        count2 = 0 
        for i in range(5):
            if visited[i][j]:
                count2 += 1
                if count2 == 5:
                    ans +=1 
            else:
                break

    # 오른 대각 : 00 11 22 33 44 
    count3 = 0
    for i in range(5):
        if visited[i][i]:
            count3 += 1
            if count3 == 5:
                ans +=1 
        else:  
            break

    # 왼 대각 : 04 13 22 31 40
    count4 = 0
    for i in range(5):
        j = 4-i
        if visited[i][j]: 
            count4 += 1
            if count4 == 5:
                ans += 1
        else:
            break

    return ans

answer = 0 # 정답
bingo = 0 # 빙고 횟수. 1이되면 종료 
visited = [[False]*5 for _ in range(5)] # 호출시 True
state = {} # 빙고판에서의 위치 
for i in range(5):
    numbers = list(map(int,input().split()))
    for j in range(5):
        state[numbers[j]] = (i,j)

for i in range(5):
    arr = list(map(int,input().split()))
    for j in range(5):
        answer += 1
        x,y = state[arr[j]]
        visited[x][y] = True
        if check() >= 3:
            bingo = 1
            break 
    
    if bingo: # bingo가 나오면 종료
        break

print(answer)