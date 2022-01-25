n = list(input())
n.sort()
# print(n)
num = 0
ans = ''

for i in n:
    if(i.isdigit()): 
        num += int(i)
    else:
        ans += i
print(ans+str(num))

