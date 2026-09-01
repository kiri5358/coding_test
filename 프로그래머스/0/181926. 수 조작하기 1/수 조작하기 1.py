def solution(n, control):
    operations = {
        'w': 1,
        's': -1,
        'd': 10,
        'a': -10
    }
    
    for char in control:
        n += operations[char]
        
    return n