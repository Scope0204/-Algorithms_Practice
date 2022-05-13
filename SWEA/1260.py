# [s/w 문제해결 기본 ] - 1일차 

# 문제 풀이 
'''
0 0 3 5 2 4 9 0 6 4 6 0 0 (맨오른쪽, 맨왼쪽 두칸은 건물이 지어지지 않음 = 0) 
좌, 우 비교해서 해당되는 입주민수의 최소값만 가져온다 -> min 
'''

for idx in range(1,11): # 10개의 테스트 수 
    answer = 0 
    n = int(input())
    graph = list(map(int,input().split()))

    for i in range(2,n-2): # 앞 뒤로 2칸은 건물이 없음 
        # 비교대상 : 뒤로 2,1칸 / 앞으로 1,2칸 -> 전부 0보다 커야함 
        
        view_ok = min(graph[i]-graph[i-2], graph[i]-graph[i-1], graph[i]-graph[i+1] ,graph[i]-graph[i+2])
        if view_ok > 0 : 
            answer += view_ok

    print("#{} {}".format(idx,answer))

                