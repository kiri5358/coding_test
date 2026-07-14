from itertools import combinations
import math

# 소수인지 판별하는 함수
def is_prime(n):
    if n < 2:
        return False
    # 2부터 n의 제곱근까지 나누어떨어지는 수가 있는지 확인
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False  # 나누어떨어지면 소수가 아님
    return True  # 모두 통과하면 소수

def solution(nums):
    answer = 0
    
    # 1. nums 배열에서 서로 다른 3개의 숫자 조합을 모두 구함
    for comb in combinations(nums, 3):
        # 2. 3개 숫자의 합을 구함
        total = sum(comb)
        
        # 3. 그 합이 소수인지 확인
        if is_prime(total):
            answer += 1
            
    return answer