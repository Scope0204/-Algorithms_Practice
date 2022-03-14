n,m,v = list(map(int,input().split()))
node = [list(map(int,input().split())) for _ in range(m)]
ans_len = []
for i in node:
    for j in i:
        ans_len.append(j)
ans_len = len(set(ans_len))
dfs_ans = [v]
bfs_ans = [v]

def dfs(num):
    stack = []
    if len(dfs_ans) == ans_len:
        return

    for n in node: 
        if num in n:
            for number in n:
                if number not in dfs_ans:
                    stack.append(number)

    stack.sort()
    dfs_ans.append(stack[0])
    dfs(stack[0])


def bfs(num):
    queue = []
    while len(bfs_ans) != ans_len:
        for n in node: 
            if num in n:
                for number in n:
                    if number not in bfs_ans:
                        queue.append(number)
    
        queue.sort()
        for q in queue:
            if q not in bfs_ans:
                bfs_ans.append(q)
        
        num = queue.pop(0)



dfs(v)
bfs(v)
print(' '.join(list(map(str,dfs_ans))))
print(' '.join(list(map(str,bfs_ans))))

