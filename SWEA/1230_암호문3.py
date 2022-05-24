for t in range(1,11):
    n = int(input())
    arr = list(map(int,input().split()))
    m = int(input())
    arr2 = list(input().split())

    comm = []
    for i in range(len(arr2)):
        if not arr2[i].isdigit(): # 명령문이 올 떄 
            if i != 0:
                comm.append(plus)
            plus = [arr2[i]]
        elif i == len(arr2)-1: # 마지막인 경우, 암호가 주어지므로 더하고 ins에 넣는다
            plus.append(int(arr2[i]))
            comm.append(plus)
        else:
            plus.append(int(arr2[i]))

    for i in comm:
        if i[0] == "I":
            x,y,s = i[1],i[2],i[3: ]
            for j in range(y):
                # x~x+y번째까지 대체 
                arr.insert(x+j, s[j])
        elif i[0] == "D":
            x,y =i[1],i[2]
            for _ in range(y):
                # x번째 arr를 y개 삭제
                arr.pop(x)

        elif i[0] == "A":
            y,s = i[1],i[2: ]
            for j in s:
                arr.append(j)
            
    print("#{}".format(t), *arr[:10])   
    