n = int(input())
arr = []
for i in range(n):
    data = input().split() 
    arr.append((data[0], int(data[1]), int(data[2]),int(data[3])))
    # 이름 , 국 , 영 , 수  


arr = sorted(arr, key= lambda x:(-x[1],x[2],-x[3],x[0])) 

for student in arr:
    print(student[0])