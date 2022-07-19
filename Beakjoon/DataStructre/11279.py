# 최대 힙 구현

import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
heap = []

for _ in range(n):
    num = int(input())
    if num == 0:
        if heap:
            print(-heapq.heappop(heap)) # 원래 값으로 바꾸기 위해 다시 치환
        else: # 비어있는 경우 
            print(0)
    
    heapq.heappush(heap,-num) # 음수로 치환하여 넣음 -> 최대 힙 정렬 
