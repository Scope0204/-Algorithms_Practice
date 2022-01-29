# 수빈이는 걷거나 순간이동을 할 수 있다
# 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 
# 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.
# https://tipsyziasu.tistory.com/130?category=956182 참고
from collections import deque

def bfs():
    q = deque([n]) # 수빈의 출발 위치
    while q:
        x = q.popleft()
        if x == k: # 같은 위치에 있는 경우
            return state[x]
        #BFS
        for nx in [x-1,x+1,x*2]: 
            if 0 <= nx <= MAX and not state[nx]:
                state[nx] = state[x] + 1
                q.append(nx)


n,k = map(int,input().split())
MAX = 100001
# n,k = 5 ,17
state = [0] * MAX  
print(bfs())




