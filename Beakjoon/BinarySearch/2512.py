n = int(input())
arr = list(map(int,input().split()))
arr.sort()
m = int(input())

start = 1
end = arr[-1]

while start<=end:
    mid = (start+end)//2

    total = 0
    for i in range(n):
        if mid < arr[i]:
            total += mid
        else:
            total += arr[i]
    
    if total <= m: 
        start = mid + 1
    else:
        end = mid - 1

print(end)
