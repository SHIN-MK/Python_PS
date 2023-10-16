from collections import deque

def solution(priorities, location):
    answer = 0
    length = len(priorities) - 1
    queue = deque(priorities)
    index = 0
    
    while queue:
        if index > length:
            index = 0
            
        priority = queue.popleft()     
        
        if priority < max(queue):
            queue.append(priority)
            index += 1
        elif index == location:
            answer += 1
            return answer
        else:
            answer += 1
            index += 1

solution([1, 1, 9, 1, 1, 1], 0)