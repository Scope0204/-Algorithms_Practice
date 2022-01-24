n = int(input())
data = list(map(int, input().split()))
data.sort() 

ans = 0 
cnt = 0 

for i in data:
    cnt += 1 
    if cnt >= i : 
        ans += 1
        cnt = 0

print(ans)
