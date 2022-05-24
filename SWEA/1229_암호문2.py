for t in range(1,11):
    n = int(input())
    arr = list(map(int,input().split()))
    m = int(input())
    arr2 = list(input().split())

    comm = []
    for i in range(len(arr2)):
        if arr2[i] == "I":
            if i != 0:
                comm.append(plus)
            plus = []
        elif arr2[i] == "D":
            if i != 0:
                comm.append(plus)
            plus = []
        elif i == len(arr2)-1: # 마지막인 경우, 암호가 주어지므로 더하고 ins에 넣는다
            plus.append(int(arr2[i]))
            comm.append(plus)
        else:
            plus.append(int(arr2[i]))

    for i in comm:
        if len(i) > 2: #insert
            x,y,s = i[0],i[1],i[2: ]
            for j in range(y):
                # x~x+y번째까지 대체 
                arr.insert(x+j, s[j])
        else: # delete
            x,y =i[0],i[1]
            for _ in range(y):
                # x번째 arr를 y개 삭제
                arr.pop(x)

    print("#{}".format(t), *arr[:10])   
    