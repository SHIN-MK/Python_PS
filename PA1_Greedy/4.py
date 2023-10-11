def solution(people, limit):
    answer = 1
    boat = []
    
    people.sort(reversed=True)
    
    for i in people:
        if sum(boat, i) > limit or len(boat) > 2:
            answer += 1
            boat.clear()
        
        boat.append(i)
    
    return answer


solution([70, 50, 80, 50], 100)