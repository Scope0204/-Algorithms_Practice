import math

def solution(fees, records):
    park = {}
    cars = {} #누적 주차 시간을 기록 
    answer = []
    
    for record in records: 
        time, car, state = record.split(" ")
        if state == "IN": # 차가 들어올 때
            park[car] = time
            if car not in cars:
                cars[car] = 0   
        else: # 나갔을 때
            in_time = park.pop(car) 
            in_hour,in_min = in_time.split(":")
            now_hour, now_min = time.split(":")

            sum_time = (int(now_hour)*60 + int(now_min)) - (int(in_hour) * 60 + int(in_min)) # 총 시간
            cars[car] += sum_time            

    if park: # 아직 나가지 않은 차가 있다면
        for car in park:
            in_hour,in_min = park[car].split(":")
            cars[car] += 1439 - (int(in_hour) * 60 + int(in_min))



    # 주차 요금 계산
    for car in sorted(cars):

        if fees[0] < cars[car] : 
            answer.append(fees[1] + math.ceil((cars[car] - fees[0])/fees[2]) * fees[3])
        else:
            answer.append(fees[1])

    return answer 

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
