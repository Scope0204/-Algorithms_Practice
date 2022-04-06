import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
node = [[] for _ in range(n+1)]
ans = [0 for _ in range(n+1)]
visited = [ False for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int,input().split())
    node[a].append(b)
    node[b].append(a)

def dfs(num):
    if not visited[num]:
        visited[num] = True

    for n in node[num]:
        if not visited[n]:
            ans[n] = num
            dfs(n)
    
dfs(1)
for i in range(2,len(ans)):
    print(ans[i])
