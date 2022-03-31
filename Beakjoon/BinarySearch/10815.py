def binarySearch(target):
    start = 0
    end = n-1
    while start<=end:
        mid = (start+end)//2

        if n_list[mid] == target:
            return '1'
        elif n_list[mid] < target: 
            start = mid + 1
        elif n_list[mid] > target:
            end = mid - 1 
    
    return '0'

n = int(input())
n_list = list(map(int,input().split()))
n_list.sort()

m = int(input())
m_list = list(map(int,input().split()))

ans = []
for card in m_list:
    ans.append(binarySearch(card))


print(' '.join(ans))
