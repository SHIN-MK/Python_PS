import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        if scoville[0] >= K:
            return answer
        elif len(scoville) == 1 and scoville[-1] < K:
            return -1
        else:
            heapq.heappush(
                scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2
            )
            answer += 1


solution([1, 2, 3, 9, 10, 12], 7)
