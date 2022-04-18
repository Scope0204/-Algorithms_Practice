import sys

sl,sr = sys.stdin.readline().strip().split()
word = list(sys.stdin.readline().strip())

keyboard = ['qwertyuiop','asdfghjkl','zxcvbnm']
keyboard_state = {}

for x in range(3):
    for y in range(len(keyboard[x])):
        keyboard_state[keyboard[x][y]] = (x,y)

l,r = keyboard_state[sl],keyboard_state[sr]

only_left = "qwertasdfgzxcv"

answer = 0 

for w in word: 
    x,y = keyboard_state[w]

    if w in only_left: 
        lx,ly = l
        answer += 1 + abs(x-lx) + abs(y-ly)
        l = x,y
    else:
        rx,ry = r
        answer += 1 + abs(x-rx) + abs(y-ry)
        r = x,y

print(answer)