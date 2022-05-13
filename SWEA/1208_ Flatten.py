# 가장 높은 곳에 있는 상자를 가장 낮은 곳으로 옮기는 작업을 덤프

for test_case in range(1,11): # 10개의 테스트 케이스 
    n = int(input()) # 덤프 횟수 
    graph = list(map(int,input().split())) 
    for _ in range(n):
        graph[graph.index(max(graph))] -= 1 
        graph[graph.index(min(graph))] += 1
    
    print("#{} {}".format(test_case,max(graph)-min(graph)))

