from collections import deque


def solution(priorities, location):
    answer = 0
    queue = deque(priorities)
    location += 1

    while queue:
        max_q = max(queue)
        priority = queue.popleft()
        location -= 1

        if priority < max_q:
            queue.append(priority)
            if location == 0:
                location = len(queue)
        else:
            if location == 0:
                answer += 1
                return answer
            else:
                answer += 1


solution([1, 1, 9, 1, 1, 1], 2)
