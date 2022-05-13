# 최다 빈수 
# 여러개인 경우 가장 큰 수 출력

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input()) # 테스트 번호
    graph = [0]*1001 
    num_list = list(map(int,input().split()))
    for num in num_list:
        graph[num] += 1 # 나올때마다 자신의 index에 1씩 추가
  	
    mode = max(graph) 
    answer = 0
    for i in range(1000,0,-1):
        if graph[i] == mode:
            answer = i 
            break
    print("#{} {}".format(test_case,answer))
            
 