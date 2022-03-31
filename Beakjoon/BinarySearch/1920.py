def binarySearch(target):
    start = 0
    end = n-1 
    while start<=end:
        mid = (start+end) //2 
        if target == a[mid]:
            return print(1)
        elif target < a[mid]: 
            end = mid-1
        else:
            start = mid+1
    return print(0)

n = int(input())
a = list(map(int,input().split()))
a.sort()
m = int(input())
m_list = list(map(int,input().split()))

for num in m_list:
    binarySearch(num)
