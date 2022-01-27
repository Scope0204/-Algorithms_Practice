n = int(input())
ans = []
for i in range(n):
    ans.append(int(input()))

ans = sorted(ans,reverse=True)

for i in ans:
    print(i, end= ' ')