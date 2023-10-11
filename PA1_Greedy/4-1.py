import itertools

def solution(people, limit):
    answer = 0
    
    while True:
        nCr = itertools.combinations(people, 2)  
        case_boat = list(map(list, nCr))
        boat = []
        
        case_boat.sort(reverse=True)
        
        for i in case_boat:
            if sum(map(int, i)) <= limit:
                boat = i
                for j in boat:
                    people.remove(j)
                answer += 1
                break
            
        if not boat:
            answer += len(people)
            break

        
    return answer


solution([70, 50, 80, 50], 100)