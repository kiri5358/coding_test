def solution(a, b, n):
    total_cola = 0  # 상빈이가 총 마신 콜라 수
    
    # 가지고 있는 빈 병(n)이 마트에 줘야 하는 빈 병(a) 이상인 동안 반복
    while n >= a:
        new_cola = (n // a) * b  # 새로 교환한 콜라 수
        total_cola += new_cola   # 총 마신 콜라 수에 누적
        
        # 남은 빈 병 = 새로 교환해서 마신 콜라 병 + 마트에 주지 못하고 남은 병
        n = new_cola + (n % a)
        
    return total_cola