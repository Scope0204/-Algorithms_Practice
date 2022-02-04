'''
def solution(n,computers):
    conn = [[-1]*n for _ in range(n)] 
    stack = [0]

    while stack:
        i = stack.pop()
        for j in range(n):
            if computers[i][j] == 1 and conn[i][j] == -1 :
                conn[i][j] = 0
                conn[j][i] = 0
                if i != j:
                    stack.append(j)

        ans = 1 
        for i in range(n):
            if conn[i].count(-1) == n  :
                ans += 1

    return ans,conn
'''
def solution(n,computers):

    def dfs(i):
        visited[i] = 1
        for j in range(n):
            if computers[i][j] and not visited[j]: #1이고, False일때 
                dfs(j)

    ans = 0
    visited = [ False for _ in range(n)]
    for i in range(n):
        if not visited[i]: # False일때
            dfs(i)
            ans += 1

    return ans

print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
print(solution(4, [[1, 1, 0, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 1]]))                
print(solution(4, [[1, 0, 0, 1], [0, 1, 0,0], [0, 0, 1,0], [1,0,0,1]]))

