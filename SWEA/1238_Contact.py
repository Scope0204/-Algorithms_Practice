for t in range(1,11):
    n,start = map(int,input().split())
    arr = list(map(int,input().split()))

    graph = [[] for _ in range(n+1)]
    visited = [False for _ in range(n+1)]

    for i in range(0,n,2):
        graph[arr[i]].append(arr[i+1])


    que = [start]
    answer = []
    visited[start] = True

    while que: 
        que_list = que
        que = [] 
        for i in que_list:
            # visited[i] = True # 여기서 방문기록을 하면 테케 4번, 10번에서 걸림
            for j in graph[i]:
                if not visited[j]:
                    visited[j] = True # 큐에 넣을때 체크를 수행해줘야 함 
                    que.append(j)

        if not que:
            answer = que_list

    
    print("#{} {}".format(t,max(answer)))

