n = int(input())
students = []
for i in range(n):
    stu = input().split()
    students.append([stu[0],int(stu[1])])

students = sorted(students, key= lambda stu:stu[1])

for student in students:
    print(student[0], end =' ')
