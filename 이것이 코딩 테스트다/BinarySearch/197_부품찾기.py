def binary_search(arr,target,start,end):
    while start<= end: 
        mid = (start+end)//2

        # 찾은 경우 
        if arr[mid] == target:
            return mid
        
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 -> 끝 값을
        elif arr[mid] > target:
            end = mid - 1

        # 중간점의 값보다 찾고자 하는 값이 큰 경우
        else:   
            start = mid+1 

    return 0 


n = int(input()) # 부품 갯수 5
arr = list(map(int,input().split())) # 각 부품의 고유 번호 
arr.sort() 
m = int(input()) # 손님이 사는 부품 종류 수
order_list = list(map(int,input().split())) # 손님이 사려고 하는 부품 번호 

for order in order_list:
    result = binary_search(arr, order, 0, n-1)
    if result:
        print('yes', end=' ')
    else:
        print('no', end=' ')
