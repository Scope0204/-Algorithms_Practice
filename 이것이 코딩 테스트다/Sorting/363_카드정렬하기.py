import heapq

n = int(input())

# 힙에 초 기 값 삽입 - 트리 구조로 데이터가 정렬 됨 
heap  = []
for _ in range(n):
    heapq.heappush(heap, int(input()) )

ans = 0 
while len(heap) != 1:
    # 가장 작은 카드 묶음 2개 꺼내기 
    one = heapq.heappop(heap) # 가장 작은 값 반환 및 삭제
    two = heapq.heappop(heap)
    # 카드 묶음을 합쳐서 다시 삽입 
    sum_value = one+two
    ans += sum_value
    heapq.heappush(heap, sum_value)

print(ans)
