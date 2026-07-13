def solution(n):
    # 0부터 n까지의 숫자를 나타내는 리스트를 만들고 모두 True(소수)로 초기화
    # (0과 1은 소수가 아니므로 False로 시작)
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    # n의 제곱근까지만 확인하면 충분합니다.
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            # i가 소수라면, i의 배수들은 모두 소수가 아니므로 False로 변경
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
                
    # True(소수)의 개수를 세어서 반환
    return is_prime.count(True)