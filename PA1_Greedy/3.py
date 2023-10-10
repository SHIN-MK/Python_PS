def solution(number, k):
    answer = ''
    max_num = 0
    point = 0
    number = list(number)
    
    i = 0
    while True:
        if int(number[i]) >= int(number[i+1]):
            max_num = max(max_num, int(number[i]))
            point = i
            i += 1
        else:
            max_num = max(max_num, int(number[i+1]))
            if int(number[point]) >= int(number[i+1]):
                del number[i]
                k -= 1
            else:
                if k >= (i+1 - point):
                    del number[point:i+1]
                    k -= (i+1 - point)
                else:
                    del number[i:(i-k):-1]
                    k = 0

        if k == 0:
            break
                
    answer = ''.join(map(str, number))
    
    return answer

solution("4177252841", 4)