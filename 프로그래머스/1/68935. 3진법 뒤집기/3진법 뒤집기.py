def solution(n):
    ternary_str = ""
    
    while n > 0:
        remainder = n % 3    
        ternary_str += str(remainder)
        n = n // 3

    answer = int(ternary_str, 3)
    
    return answer