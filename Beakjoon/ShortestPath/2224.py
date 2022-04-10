import sys
input = sys.stdin.readline

n = int(input())
arr = [[0]*123 for _ in range(123)] # A(65) ~ z(122)

for i in range(n):
    x = list(input().split())  
    p,q = ord(x[0]),ord(x[-1])
    arr[p][q] = 1 

for k in range(123):
    for a in range(123):
        for b in range(123):
            if a!=k and k!=b and arr[a][k] and arr[k][b]: 
                arr[a][b] = 1

ans = []
for i in range(123):
    for j in range(123):
        if i != j and arr[i][j]:
            ans.append(chr(i)+" => "+chr(j))

# 정답
print(len(ans))
for answer in ans:
    print(answer)
