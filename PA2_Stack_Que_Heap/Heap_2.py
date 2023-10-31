import heapq
from collections import deque


def solution(jobs):
    start_time = 0
    during_time = 0
    total_time = 0
    length = len(jobs)
    process = deque()
    heapq.heapify(jobs)

    while jobs or process:
        if jobs and jobs[0][0] <= total_time:
            process.append(heapq.heappop(jobs))
        elif not process:
            process.append(heapq.heappop(jobs))
        else:
            process = deque(sorted(process, key=lambda x: x[1]))
            start_time, during_time = process[0][0], process[0][1]
            total_time += total_time - start_time + during_time
            process.popleft()

    answer = int((total_time - (length - 2)) / length)
    return answer


solution([[0, 3], [2, 9], [3, 6], [3, 8], [4, 7]])
