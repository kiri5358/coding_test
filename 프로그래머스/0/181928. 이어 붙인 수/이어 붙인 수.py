def solution(num_list):
    odd_str = ""  # 홀수를 이어 붙일 문자열
    even_str = "" # 짝수를 이어 붙일 문자열
    
    for num in num_list:
        if num % 2 != 0:  # 홀수인 경우
            odd_str += str(num)
        else:            # 짝수인 경우
            even_str += str(num)
            
    # 각각 숫자로 변환한 뒤 합을 반환 (빈 문자열일 경우 0으로 처리)
    return int(odd_str or 0) + int(even_str or 0)