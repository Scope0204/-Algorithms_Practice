import itertools

t = int(input())

for i in range(1,t+1):
    n = list(map(str,input()))
    possible = 0
    num = int(''.join(n))
    for j in list(map(''.join,itertools.permutations(n))):
        if int(j) != num and int(j) % num == 0: 
            print("#{} {}".format(i,"possible"))
            possible = 1
            break
    
    if not possible:
        print("#{} {}".format(i,"impossible"))