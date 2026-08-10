def solution(money):
    ice = money // 5500
    m = money - (ice*5500)
    answer = [ice, m]
    return answer