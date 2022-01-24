n,m = map(int, input().split())

answer = 0 

for i in range(n):
    data = list(map(int,input().split()))
    # 가장 작은 수 
    min_val = min(data)
    # 가장 작은 수 중에서 가장 큰 수 찾기
    answer = max(answer, min_val)

print(answer)