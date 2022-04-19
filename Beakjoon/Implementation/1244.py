import sys

def change(i):
    if switch[i] == 1 :
        switch[i] = 0 
    else:
        switch[i] = 1 

n = int(input()) # 스위치 갯수 
switch = [-1] + list(map(int,sys.stdin.readline().strip().split()))
students = int(sys.stdin.readline().strip()) # 학생 수
student = [] # 학생 정보 
for i in range(students):
    student.append(list(map(int,sys.stdin.readline().strip().split()))) 

for s in student:
    sex,number = s[0],s[1]
    if sex == 1: # 남자인 경우
        for i in range(number,len(switch),number):
            change(i)

    else : # 여자인 경우 
        count = 1
        while 1: 
            if number-count>= 0 and number+count <=len(switch)-1 : # 범위내에 속하는지
                if switch[number-count] == switch[number+count]: # 속하며 대칭되는 수가 같은 경우
                    count +=1 
                else: # 아닌 경우
                    for i in range(number-count+1, number+count):
                        change(i)
                    break
            else: 
                for i in range(number-count+1, number+count):
                    change(i)
                break
                    

for i in range(1, n+1):
    print(switch[i], end = " ")
    if i % 20 == 0 :
        print()
