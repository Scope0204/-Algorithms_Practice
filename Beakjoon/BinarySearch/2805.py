n,m = map(int,input().split())
trees = list(map(int,input().split()))
trees.sort()

start = 1 
end = trees[-1]

while start<=end:
    mid = (start+end)//2 

    total = 0 
    for tree in trees:
        if mid < tree:
            total += tree-mid
            if total > m:
                break
        
    if total >= m:
        start = mid+1
    else:
        end = mid-1

print(end)