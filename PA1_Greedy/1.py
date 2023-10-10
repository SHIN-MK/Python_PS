def solution(n, lost, reserve):
    answer = 0
    who_lost = set(lost) - set(reserve)
    who_reserve = set(reserve) - set(lost)
    
    for i in who_reserve:
        if i-1 in who_lost:
            who_lost.remove(i-1)
        elif i+1 in who_lost:
            who_lost.remove(i+1)
    
    
    return n - len(who_lost)

solution(5, [1, 3, 2, 4], [1, 3, 5])