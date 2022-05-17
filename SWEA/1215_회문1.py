def check(str):
    for i in range(len(str)//2):
        if str[i] != str[-i-1]:
            return False
    return True 

for test_case in range(1,11):
    length = int(input()) #회문 길이 
    arr = [ input() for _ in range(8)] 
    arr2= []
    for i in range(8):
        str =""
        for j in range(8):
            str += arr[j][i]
        arr2.append(str)
        
    answer = 0
    for i in range(8):
        for j in range(8-length+1):
            if check(arr[i][j:j+length]):
                answer += 1 
            if check(arr2[i][j:j+length]): 
                answer += 1
  	
    print("#{} {}".format(test_case,answer))
                