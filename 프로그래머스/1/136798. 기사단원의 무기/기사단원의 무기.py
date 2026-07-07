def solution(number, limit, power):
    total_iron = 0
    
    for i in range(1, number + 1):
        divisors_count = 0
        # 제곱근까지만 확인하여 약수의 개수를 계산
        for j in range(1, int(i**0.5) + 1):
            if i % j == 0:
                divisors_count += 1
                if j**2 != i:  # 제곱수가 아니라면 대칭되는 약수도 추가
                    divisors_count += 1
                    
        # 제한수치를 초과하는지 확인 후 철의 무게 합산
        if divisors_count > limit:
            total_iron += power
        else:
            total_iron += divisors_count
            
    return total_iron