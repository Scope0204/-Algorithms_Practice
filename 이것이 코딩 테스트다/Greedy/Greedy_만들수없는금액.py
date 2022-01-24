n = int(input())
data = list(map(int,input().split()))
data.sort()
ans = 1 

for x in data:
    print(ans,x)
    if ans < x:
        print(ans,x)
        break
    ans += x

print(ans)