def solution(new_id):
    answer = ''
    shiftstring = '~!@#$%^&*()=+[{]}:?,<>/'
    
    while True:
        length = len(new_id)
        
        if new_id.upper() == new_id.lower():
            if any(i in new_id for i in shiftstring) == False:
                if '..' not in new_id:
                    if new_id.startswith('.') or new_id.endswith('.') == False:
                        if(length > 2 and length < 16):
                            answer = new_id
                            break
        else:
            if new_id.islower():
                if any(i in new_id for i in shiftstring) == False:
                    if '..' not in new_id:
                        if new_id.startswith('.') or new_id.endswith('.') == False:
                            if(length > 2 and length < 16):
                                answer = new_id
                                break               
        
                                
        if new_id.isupper():
            new_id = new_id.lower()
        
        if any(i in new_id for i in shiftstring):
            for i in shiftstring:
                new_id = new_id.replace(i,'')
            
        while True:    
            if '..' in new_id:
                new_id = new_id.replace('..', '.')
            else:
                break
            
        if new_id.startswith('.') or new_id.endswith('.') == True:
            if new_id.startswith('.'):
                new_id = new_id[1:]
            else:
                new_id = new_id[:-1]
                
        length = len(new_id)
            
        if length <= 2 or length >= 16:
            if not new_id:    
                new_id = 'a'
            else:
                if length >= 16:
                    new_id = new_id[:-(length-15)]
                    if new_id.endswith('.'):
                        new_id = new_id[:-1]
                else:
                    if length <= 2:
                        while True:
                            new_id = new_id + new_id.strip()[-1]
                            length += 1
                            
                            if length == 3:
                                break
    
    
    return answer

new_id = "asdbasd"

print(solution(new_id))