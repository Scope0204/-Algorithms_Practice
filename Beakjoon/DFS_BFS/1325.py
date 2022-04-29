import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
computers = [[] for _ in range(n+1)]
state = [False for _ in range(n+1)]
connect = [0 for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    computers[b].append(a)


def solution(idx):
    conn = 1 # 최소 자기자신 1개는 해킹할 수 있으니까 
    que = deque([idx])
    state = [False for _ in range(n+1)]
    state[idx] = True 

    while que:
        i = que.popleft()

        for ni in computers[i]:
            if not state[ni]: 
                state[ni] = True
                conn += 1 
                que.append(ni)
    return conn


max_conn = 0
answer = []

for i in range(1,n+1):
	conn = solution(i)
	if conn > max_conn:
		max_conn = conn
		answer.clear()
		answer.append(i)
	elif conn == max_conn:
		answer.append(i)

print(*answer)    
