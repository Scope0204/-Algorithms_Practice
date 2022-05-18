for t in range(1,11):
    n = int(input())
    test_case = list(input())
    stack = [] 

    left = ['(','[','{','<']
    right = [')',']','}','>']
    
    answer = 1 # 1 = 유효, 0 = 유효하지 않음
    for i in range(n):
        if test_case[i] in left: # 왼쪽 괄호
            stack.append(test_case[i])
        else: # 오른쪽 괄호
            if right.index(test_case[i]) == left.index(stack[-1]):
                stack.pop()
            else:
                answer = 0 
                break
    
    print("#{} {}".format(t,answer))
