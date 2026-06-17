def solution(s):
    answer = []
    idx = 0 
    
    for char in s:
        if char == " ": 
            answer.append(char)
            idx = 0 
        else:
            if idx % 2 == 0:
                answer.append(char.upper())
            else:
                answer.append(char.lower())
            idx += 1
            
    return "".join(answer)