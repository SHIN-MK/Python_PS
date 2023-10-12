def solution(routes):
    answer = len(routes)
    routes.sort(key=lambda x: x[1])
    and_area = []
    
    while len(routes):
        i, j = routes.pop(0)
        k = 0
        
        if not and_area:
             and_area.append([i, j])
        else:
            for k in range(len(and_area)):
                if and_area[k][0] > j or and_area[k][1] < i:
                    and_area.append([i, j])
                else:
                    if i <= and_area[k][0] and j >= and_area[k][1]:
                        answer -= 1
                    elif i > and_area[k][0] and j < and_area[k][1]:
                        and_area[k][0] = i
                        and_area[k][1] = j
                        answer -= 1
                    else:
                        if i <= and_area[k][0]:
                            and_area[k][0] = i
                            answer -= 1
                        else:
                            and_area[k][1] = j
                            answer -= 1
                
    return answer

solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]])