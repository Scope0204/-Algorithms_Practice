# 주어진 수들을 M번 더하여 가장 큰 수를 만듬. K번 초과해서 더할 수 없음
# 5 8 3 -> 8번 더하는데 연속해서 3번 초과해서 더할 수 없음
'''
N,M,K = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

first = data[-1] # 가장 큰 수 
second = data[N-2] # 두번째로 큰 수
count = 0
answer = 0

for i in range(M):
    if count == K : # K번 반복할 때, second출력 후 초기화 
        answer += second
        count = 0
    else: 
        answer += first 
        count += 1 # 횟수 카운트

print(answer)
'''
N,M,K = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

first = data[-1] # 가장 큰 수 
second = data[N-2] # 두번째로 큰 수

count = int(M/(K+1))* K 
count += M % (K+1)

answer = 0 
answer += count * first
answer += (M-count) * second # 남은 수는 두번째로 큰 수가 들어간 자리

print(answer)