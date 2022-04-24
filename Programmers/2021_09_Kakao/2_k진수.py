def change(n, k):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, k) # 몫, 나머지
        rev_base += str(mod)

    return rev_base[::-1] 
    # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력

def is_prime_number(x):
    # 2부터 (x - 1)까지의 모든 수를 확인
    if x == 1:
        return False
    elif x == 2 :
        return True
    else: 
        for i in range(3, int(x**0.5) +1 , 2): # 이부분에서 막힘 
            if x % i == 0: # x가 해당 수로 나누어떨어지면
                return False
    return True


def solution(n, k):
    answer = 0  
    check_num = change(n,k).split('0') # k 진수로 변환
    print(check_num)
    for num in check_num : 
        if num and is_prime_number(int(num)): #소수 체크
            answer += 1

    return answer

print(solution(110011,10))
