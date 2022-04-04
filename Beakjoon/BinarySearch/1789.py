s = int(input()) # 서로 다른 n개의 자연수 합
n = 1 

while n * (n+1) / 2 <= s: 
    n += 1
     
print(n -1)