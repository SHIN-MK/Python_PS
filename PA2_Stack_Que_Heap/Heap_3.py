import heapq


def solution(operations):
    answer = []
    heap_list = []

    for i in operations:
        heap_min = []
        heap_max = []
        for j in heap_list:
            heapq.heappush(heap_min, j)
            heapq.heappush(heap_max, (-j, j))

        if "I" in i:
            num = int(i[2:])
            heap_list.append(num)

        else:
            if heap_list and i == "D -1":
                tmp = heapq.heappop(heap_min)
                heap_list.remove(tmp)

            elif heap_list and i == "D 1":
                tmp = heapq.heappop(heap_max)
                heap_list.remove(tmp[1])

    if not heap_list:
        answer = [0, 0]
    else:
        heap_min = []
        heap_max = []
        for j in heap_list:
            heapq.heappush(heap_min, j)
            heapq.heappush(heap_max, (-j, j))
        answer = [heap_max[0][1], heap_min[0]]

    return answer


solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"])
