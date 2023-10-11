def solution(number, k):
    answer = ''
    big_number = []
    number = list(number)

    i = 0 
        
    while k != 0:
        if not big_number:
            big_number.append(number[i])
            i += 1
        else:
                if big_number[-1] < number[i]:
                    big_number.pop()
                    big_number.append(number[i])
                    k -= 1
                    i += 1
                elif big_number[-1] > number[i]:
                    if number[i] > number[i-1]:
                        big_number.append(number[i])
                        i += 1
                    else:
                        i += 1
                        k -= 1
                else:
                    big_number.append(number[i])
                    i += 1

    big_number.extend(number[i:])
            
    answer = ''.join(big_number)
    return answer

solution("93939", 2)