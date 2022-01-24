n,k = map(int,input().split())
ans = 0 

while n != 1:
    if n%k == 0: # 나누어 지면
        n = n//k
    else:
        n -= 1 # 안 나누어 지면 -1
    
    ans += 1

print(ans)