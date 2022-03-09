# from itertools import permutations

# n = int(input())
# num= list(map(int,input().split()))
# op_idx = list(map(int,input().split()))  # +, -, *, /
# operator = ['+','-','*','/']
# op = []
# for i in range(4): 
#     for j in range(op_idx[i]):
#         op.append(operator[i])

# # set을 이용한 중복제거
# op = list(set(permutations(op,len(op)))) 

# answer = [] 

# for i in op:
#     number = num[0]
#     for j in range(n-1): # 연산자 수 = n-1개
#         if i[j] == '+':
#             number += num[j+1]
#         elif i[j] == '-':
#             number -= num[j+1]
#         elif i[j] == '*':
#             number *= num[j+1]
#         else: # / 일떄
#             if number // num[j+1] < 0: # 음수//양수 연산 
#                 number = -(-number//num[j+1])
#             else: 
#                 number = number//num[j+1]
#     answer.append(number)
    
# print(max(answer))
# print(min(answer))

# 백트래킹 (Python3 통과, PyPy3도 통과)
import sys

input = sys.stdin.readline
N = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))  # +, -, *, //

maximum = -1e9
minimum = 1e9


def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus:
        dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / num[depth]), plus, minus, multiply, divide - 1)


dfs(1, num[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)