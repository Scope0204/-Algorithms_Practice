'''
sound = list(input())
duck = 0 
duck_sound = {0:'q', 1:'u', 2:'a', 3:'c',4:'k'} 
now = []

def sound_check(length,s):
    if duck_sound[length] == s:
        return True
    else:
        False 

if len(sound) % 5 != 0:
    print(-1)  

else:
    for s in sound:
        if s == 'q':
            now.append(['q']) # 새롭게 추가
            if duck:
                duck -= 1
        else:
            for i in range(len(now)):
                if len(now[i]) < 5 and sound_check(len(now[i]),s):
                    now[i].append(s)
                    if len(now[i]) == 5:
                        duck += 1
                    break
    
    # print(duck,now)
    for arr in now:
        if len(arr) != 5:
            duck = 0

    print(duck if duck else -1)


'''
# 올바른 풀이
import sys

input_duck = sys.stdin.readline().strip()

str_length = len(input_duck)

visited = [0] * str_length

goal_str = "quack"

duck_count = 0

#글자 수가 5의 배수가 아니면 -1
if str_length%5 != 0:
    print(-1)

else:
    for i in range(str_length):

        # q(시작)이고 방문하지 않았다면, quack을 찾는 탐색 시작
        if input_duck[i] == "q" and visited[i] == 0:

            count = 0
            check = True
            for j in range(i,str_length):
                if input_duck[j] == goal_str[count] and visited[j] == 0:
                    visited[j] = 1
                    if input_duck[j] == "k":
                        if check == True:
                            duck_count += 1
                            check = False
                        count = 0
                        continue
                        
                    count+=1

    if duck_count == 0 or 0 in visited:
        print(-1)

    else:
        print(duck_count)


