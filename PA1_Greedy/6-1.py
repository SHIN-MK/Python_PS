def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    c = -30001
    
    for i in routes:
        if c < i[0]:
            answer += 1
            c = i[1]
            
    return answer

solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]])