S = input()
ans = int(S[0]) 

for i in range(1,len(S)): 
    num = int(S[i])
    if num <= 1 or ans <= 1:
        ans += num
    else:
        ans *= num
        
print(ans)
