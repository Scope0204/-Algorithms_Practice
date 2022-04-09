# 모든 정점 (i, j)에 대해서, i에서 j로 가는 경로가 있는지 없는지 구하는 프로그램을 작성하시오.
# i번째 줄의 j번째 숫자가 1인 경우에는 i에서 j로 가는 간선이 존재한다는 뜻이고, 0인 경우는 없다는 뜻이다. 
# i번째 줄의 i번째 숫자는 항상 0이다.

import sys
input = sys.stdin.readline

n = int(input())
g = [ list(map(int,input().split())) for _ in range(n)]

# 플로이드 워셜 알고리즘 수행
for k in range(n):
    for a in range(n):
        for b in range(n):
            if g[a][k] and g[k][b]:
                g[a][b] = 1

# 결과 
for arr in g:
    ans = ""
    for num in arr:
        ans += str(num)+" "
    print(ans)