from collections import deque


def solution(prices):
    answer = []
    prices = deque(prices)

    while prices:
        time = 0
        tmp = prices.popleft()
        if prices:
            for i in prices:
                if tmp <= i:
                    time += 1
                    if time >= len(prices):
                        answer.append(time)
                else:
                    time += 1
                    answer.append(time)
                    break
        else:
            answer.append(time)

    return answer


solution([1, 2, 3, 2, 3])
