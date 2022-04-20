import sys

n = int(sys.stdin.readline().strip()) 
extensions = {}
for i in range(n):
    extension = sys.stdin.readline().strip().split('.')[1]
    if extension in extensions:
        extensions[extension] += 1 
    else: 
        extensions[extension] = 1 


for e in sorted(extensions.keys()):
    print(e+' '+str(extensions[e]))


