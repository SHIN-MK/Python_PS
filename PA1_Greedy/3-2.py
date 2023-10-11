def solution(number, k):
    answer = ''
    big_number = []
    
    for i in number:
        while True:
            if k > 0 and big_number and big_number[-1] < i:
                big_number.pop()
                k -= 1
            else:
                break
                
        big_number.append(i)
    
    answer = ''.join(big_number[:len(big_number) - k])
    
    return answer

solution("4177252841", 4)