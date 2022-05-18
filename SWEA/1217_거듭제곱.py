# 총 n번의 재귀가 일어나야한다  
# 마지막 n번째에서는 제곱이 0이 되며 return이 일어나기때문에 재귀함수호출이 종료된다 
# 그때부터 1*num*num ... (n번) = num**n의 값이 됨
def solution(num,n):
    if n == 0:
        return 1
    else: 
        return num * solution(num,n-1)


for _ in range(10):
    t = int(input())
    num,n = map(int,input().split())
    
    # 조건 : 재귀를 사용해서 풀 것 
    answer = solution(num,n)

    print("#{} {}".format(t,answer))