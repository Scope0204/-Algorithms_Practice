data = input() 
row = int(data[1])
col = int(ord(data[0])) - int(ord('a')) + 1 
# ord() 아스키 코드 반환. 

# 나이트가 이동할 수 있는 방향
# 총 8가지 방법이있다. 
steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

ans= 0 
for step in steps:
    # 이동하는 위치 확인 
    next_row = row + step[0]
    next_col = col + step[1]
    print(next_row,next_col)
    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <=8: 
        # 이동 후 범위는 1~8안에 있어야만 한다 
        ans += 1

print(ans)