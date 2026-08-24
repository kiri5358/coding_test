def solution(a, b, c):
    # 세 숫자가 모두 다른 경우
    if a != b and b != c and a != c:
        return a + b + c
    
    # 세 숫자가 모두 같은 경우
    elif a == b and b == c:
        return (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
    
    # 어느 두 숫지만 같은 경우 (나머지 하나는 다른 경우)
    else:
        return (a + b + c) * (a**2 + b**2 + c**2)