import sys
input = sys.stdin.readline

N = int(input()) 
star = [[" " for _ in range(4*N - 3)] for _ in range(4*N - 3)]

def solution(n,x,y):
    
    if n == 1:
        star[x][y] = '*'
        return
    else:
        length = 4*n - 3
        print(length)
        for i in range(length):
            star[x][y+i] = '*'
            star[x+i][y] = '*'
            star[x+length-1][y+i] = "*"
            star[x+i][y+length-1] = '*'
    solution(n-1, x+2, y+2)
    
solution(N,0,0)

for i in star:
    print(''.join(i))
 

