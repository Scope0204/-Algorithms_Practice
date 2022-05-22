test_case = int(input())
number = {"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9
} 
number2 = {0:"ZRO", 1:"ONE", 2:"TWO", 3:"THR", 4:"FOR", 5:"FIV", 6:"SIX", 7:"SVN", 8:"EGT", 9:"NIN"
} 

for _ in range(test_case):
    t,n = input().split()
    n = int(n)

    # 무작위 숫자 리스트 
    num_list = list(input().split())

    # 갯수 체크용 리스트
    count = [0]*10

    for i in range(n):
        count[number[num_list[i]]]+= 1

    answer = []
    for i in range(10):
        for _ in range(count[i]):
            answer.append(number2[i])
            

    print(t)
    print(*answer)