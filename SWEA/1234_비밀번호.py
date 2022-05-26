for t in range(1,11):
    n,password = input().split()

    password = list(password)

    while 1:
        temp = True

        for i in range(len(password)-1):
            if password[i] == password[i+1]:
                del password[i:i+2]
                temp = False
                break
        
        if temp:
            break

    print("#{} {}".format(t,''.join(password)))

# 다른 풀이 : stack을 이용
# https://devlibrary00108.tistory.com/279