from itertools import combinations

t = int(input())

for test_case in range(1,t+1):
    n,k = map(int,input().split()) 
    p = list(map(int,input().split()))

    answer = 0
    # 1,2,3, .. n개 조합
    for i in range(n):
        for j in combinations(p,i):
            if k == sum(j):
                answer += 1

    print("#{} {}".format(test_case,answer))


