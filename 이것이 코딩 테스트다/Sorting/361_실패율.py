# 실패율 : 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
def solution(N,stages):
    length = len(stages)
    users = []

    for i in range(1,N+1): 
        count = stages.count(i)

        # 실패율 계산
        if length == 0:
            fail = 0 
        else:
            fail = count / length

        users.append((i, fail))
        length -= count
    
    users = sorted(users, key=lambda x : x[1], reverse= True)
    # print(users)
    ans = [user[0] for user in users]
    return ans

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))
print(solution( 4, [4,4,4,4,4]))
