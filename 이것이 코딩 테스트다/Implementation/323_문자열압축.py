def solution(s):
    answer = len(s)

    for step in range(1,len(s)//2 + 1):
        # step : 1~len(s)//2 까지 단계를 늘려가며 함
        compressed = "" # 압축하여 나온 문자열
        prev = s[0:step] # 앞에서부터 step만큼의 문자열 추출
        cnt = 1 # 압축횟수 
        # step 크기만큼 증가시키며 이전 문자열과 비교
        for i in range(step, len(s),step):
            # 이전 상태와 동일한 경우 cont 증가
            if prev == s[i:i+step]: 
                cnt += 1
            # 다른 문자열이 나온 경우 = 더 이상 압축불가
            else:
                # 2번이상은 압축한 경우에만 cnt를 형변환해서 앞에붙여주고, 아닌경우 그냥 prev
                compressed += str(cnt) + prev if cnt >= 2 else prev  
                prev = s[i:i+step] # 이제 해당문자열과 비교해주기 위해 상태 초기화
                cnt = 1 # 압축 횟수도 초기화 
            
        # 남아있는 문자열도 조건에 맞게 뒤에 추가함
        compressed += str(cnt) + prev if cnt >= 2 else prev

        # 만들어지는 압축 문자열이 가장 짧은 것이 정답
        answer = min(answer,len(compressed)) # 최초 answer은 입력받은 s 의 길이 
        # 압축이 전혀안되는 경우에는 기존 s의 길이가 나올 것임
        
    return answer