def solution(code):
    ret = ''
    mode = 0 
    
    for idx, char in enumerate(code):
        if char == "1":
            mode = 1 - mode
        else:
            if idx % 2 == mode:
                ret += char
                
    if ret == "":
        return "EMPTY"
    else:
        return ret