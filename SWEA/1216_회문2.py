#거꾸로 읽어도 같은의미의 문자를 "회문"이라고 함
#회문을 검사하는 함수
def check(str):
    for i in range(len(str)//2):
        if str[i] != str[-i-1]:
            return False
    return True

for _ in range(10):
    t = int(input())
    arr = [input() for _ in range(100)]
    arr2 = [] # 세로축으로 되어있는 문자열이 저장되어 있음
    for i in range(100):
        str = ""
        for j in range(100):
            str += arr[j][i]
        arr2.append(str) 

    
    answer = 0
    for length in range(100,1,-1):
        if answer >=length: # 100 부터 1의 회문의 길이를 구했으므로, 답을 구한 이후에는 무조건 작을수밖에없다
            break # for문 완전 탈출 
        for i in range(100):
            if answer == length: # = 3번째 for문에서 답을 구했을 경우 
                break # 2번째 for문 탈출
            for j in range(100-length+1):
                if check(arr[i][j:j+length]) or check(arr2[i][j+length]):
                    answer = length # 답은 해당 길이가 된다
                    break # 3번째 for문 탈출 
            
    print("#{} {}".format(t,answer))

