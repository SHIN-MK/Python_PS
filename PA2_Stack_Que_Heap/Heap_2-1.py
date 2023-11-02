import heapq


def solution(jobs):
    answer = 0
    endTime = 0
    reqTime = 0
    durTime = 0
    process = []
    heapq.heapify(jobs)

    while jobs:
        reqTime, durTime = heapq.heappop(jobs)
        if endTime == 0:
            endTime = reqTime + durTime
            answer += endTime
            currentTime += 1
        
        if process
            
            

        
        
    return answer


solution([[0, 3], [1, 9], [2, 6]])
