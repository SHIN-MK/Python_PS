import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    many = 0
    date = 0
    datelist = deque()
    
    for x, y in zip(progresses, speeds):
        datelist.append(math.ceil((100-x) / y))
    
    while datelist:
        if date >= datelist[0]:
            while datelist and date >= datelist[0]:
                datelist.popleft()
                many += 1
            answer.append(many)
            many = 0
        else:
            date += 1
   
    return answer

solution([93, 30, 55], [1, 30, 5])