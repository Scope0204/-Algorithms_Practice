def dfs(num,count):
    if num > b: # 더 이상 연산이 의미가 없는 경우 
        return 
    elif num == b: # 같아진 경우
        ans.append(count)
        return 
    else:
        dfs(num*2, count+1) # 연산 1 : 2곱하기 
        dfs(int(str(num)+'1'), count+1) # 연산 2 : 1을 가장 오른쪽에 추가 
        

    
    return 

a,b = map(int,input().split())
ans = []
dfs(a,0)
if ans:
    print(min(ans)+1)
else:
    print(-1)

