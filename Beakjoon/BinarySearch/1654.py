'''
mid = (0+802) //2 = 402 
802 // 402 = 2
742 // 402 = 1
457 // 402 = 1
539 // 402 = 1 
total = 5 
5 < n (= 11) 
=> mid가 좀더 왼쪽에 있다. 
'''
k,n = map(int,input().split())
lan = [ int(input()) for _ in range(k)]
lan.sort() 

start = 1 
end = lan[-1]

while start<=end: 
    total = 0
    mid = (start+end)//2
    
    for i in lan:
        total += i//mid 
        
    if total >= n: 
        start = mid + 1
    
    else:
        end = mid - 1

print(end)

