for t in range(1,11):
    n = int(input())
    arr = list(map(int,input().split()))
    m = int(input()) # 명령어 갯수
    comm = list(input().split())

    ins = []
    for i in range(len(comm)):
        if comm[i] == "I":
            if i != 0:
                ins.append(plus)
            plus = []
        elif i == len(comm)-1: # 마지막인 경우, 암호가 주어지므로 더하고 ins에 넣는다
            plus.append(int(comm[i]))
            ins.append(plus)
        else:
            plus.append(int(comm[i])) # 0,1,2~ = x,y,s

    # ins = [ [plus], [plus] ... ]
    for i in ins:
        x = i[0]
        y = i[1]
        s = i[2: ]
        for j in range(y):
            # x~x+y번째까지 대체 
            arr.insert(x+j, s[j])
        
    print("#{}".format(t), *arr[:10])   

