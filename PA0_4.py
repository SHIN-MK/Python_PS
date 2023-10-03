def solution(new_id):
    answer = ''
    
    while True:
        length = len(new_id)
        print(length)    
        if new_id.islower():
            print('소문자임\n')
            if any(i in new_id for i in '~!@#$%^&*()=+[{]}:?,<>/') == False:
                print('특수기호 잘씀\n')
                if '..' not in new_id:
                    print('.이 연속되지 않음\n')
                    if new_id.startswith('.') or new_id.endswith('.') == False:
                        print('.으로 시작되거나 끝나지 않음\n')
                        if(length > 2 and length < 16):
                            print('완벽하노\n')
                            answer = new_id
                            break
                        else:
                            if not new_id:    
                                new_id = 'a'
                            else:
                                if length >= 16:
                                    new_id = new_id[:-(length-15)]
                                    if new_id.endswith('.'):
                                        new_id = new_id[:-1]
                                else:
                                    if length <= 2:
                                        for length in 3:
                                            new_id += new_id.strip()[-1]
                                            length += 1
                                            
                    else:
                        if new_id.startswith('.'):
                            new_id = new_id[1:]
                        else:
                            new_id = new_id[:-1]               
                else:
                   new_id.replace('..', '.')
            else:
                new_id.translate({ord(letter): None for letter in '~!@#$%^&*()=+[{]}:?,<>/'})
        else:
            new_id.lower()
                        
    return answer

new_id = '=.='

print(solution(new_id))
