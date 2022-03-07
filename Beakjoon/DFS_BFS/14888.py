from itertools import permutations

n = int(input())
num= list(map(int,input().split()))
op_idx = list(map(int,input().split()))  # +, -, *, /
operator = ['+','-','*','/']
op = []
for i in range(4): 
    for j in range(op_idx[i]):
        op.append(operator[i])

# set을 이용한 중복제거
op = list(set(permutations(op,len(op)))) 

answer = [] 

for i in op:
    number = num[0]
    for j in range(n-1): # 연산자 수 = n-1개
        if i[j] == '+':
            number += num[j+1]
        elif i[j] == '-':
            number -= num[j+1]
        elif i[j] == '*':
            number *= num[j+1]
        else: # / 일떄
            if number // num[j+1] < 0: # 음수//양수 연산 
                number = -(-number//num[j+1])
            else: 
                number = number//num[j+1]
    answer.append(number)
    
print(max(answer))
print(min(answer))