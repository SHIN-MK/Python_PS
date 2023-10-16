from collections import deque

def solution(priorities, location):
    answer = 0
    length = len(priorities) - 1
    queue = deque(priorities)
    index = 0
    outindex = []
    
    while queue:
        if index > length:
            index = 0
        
        while index in outindex:
            index += 1
            
        priority = queue.popleft()     
        
        if index <= length:
            if queue and priority < max(queue):
                queue.append(priority)
                index += 1
            elif index == location:
                answer += 1
                return answer
            else:
                answer += 1
                outindex.append(index)
                index += 1

solution([1, 2, 3, 4, 3, 2, 1], 0)