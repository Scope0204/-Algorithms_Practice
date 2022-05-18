#  A도시에서 B도시로 가는 길이 존재하는지 알아내는 프로그램을 작성하여라. 있으면 1 없으면 0 
# 출발은 0 도착점은 99 
def dfs(num):
    visited[num] = True

    for i in graph[num]:
        if not visited[i]: 
            dfs(i)

for i in range(10):
    t,n = map(int,input().split()) # 테스트 케이스의 번호, 길의 총 개수 
    arr = list(map(int,input().split())) # 짝수는 출발지 , 홀수는 갈 수 있는 길 
    graph = [[] for _ in range(100)]
    visited = [ False for _ in range(100)]
    
    for i in range(0,n*2,2):
        graph[arr[i]].append(arr[i+1])

    dfs(0) 
    answer = 1 if visited[99] else 0
    print("#{} {}".format(t,answer))