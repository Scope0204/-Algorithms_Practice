t = 10

for _ in range(t):
    n = int(input())
    password = list(map(int,input().split()))
    
    count = 0
    while 1:
  
        if count == 5:
            count = 1
        else: 
            count += 1

        number = password.pop(0) - count
        
        if number <= 0:
            number = 0
            password.append(number)
            break
        else:
            password.append(number)
    
    print("#{}".format(n),*password)

