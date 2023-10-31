from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 1
    eachTime = deque()
    queue = deque(truck_weights)
    crossingTruck = deque()

    while queue or crossingTruck:
        if not crossingTruck:
            crossingTruck.append(queue.popleft())
            eachTime.append(0)
        elif queue and sum(crossingTruck) + queue[0] <= weight:
            crossingTruck.append(queue.popleft())
            eachTime.append(0)

        for i in range(len(eachTime)):
            eachTime[i] += 1

        if eachTime[0] == bridge_length:
            crossingTruck.popleft()
            eachTime.popleft()

        answer += 1
    return answer


solution(2, 10, [7, 4, 5, 6])
