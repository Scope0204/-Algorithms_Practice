n,m = map(int,input().split()) # 떡의 개수 , 요청한 떡의 길이 
arr = list(map(int,input().split())) # 떡의 개별 높이 정보 
arr.sort()

start = 0 
end = arr[-1] 

#이진 탐색 수행(반복적)
result = 0 
while(start<= end):
    total = 0 
    mid = (start+end)//2
    for x in arr:
        # 잘랐을 때 떡의 양 계산
        if x > mid:
            total += x - mid 

    # 떡의 양이 부족한 경우 더 많이 자르기 
    if total < m :
        end = mid -1
    
    # 떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
    else:
        result = mid # 최대한 덜 잘랐을 떄가 정답이므로, 여기에서 result에 기록
        start = mid + 1 

# 정답 출력
print(result)



