import sys, heapq

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
heap = []

for _ in range(n):
    num = int(input())
    if num == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)

    else:
        heapq.heappush(heap,(abs(num),num))