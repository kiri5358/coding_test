def solution(n, arr1, arr2):
    answer = []
    for num1, num2 in zip(arr1, arr2):
        # 1. 두 지도의 숫자를 비트 OR 연산합니다.
        combined = num1 | num2
        
        # 2. 이진수 문자열로 변환하고, 앞의 '0b'를 제거합니다.
        binary_str = bin(combined)[2:]
        
        # 3. 한 변의 길이 n만큼 앞자리에 0을 채워줍니다.
        binary_str = binary_str.zfill(n)
        
        # 4. 1은 '#'으로, 0은 공백(' ')으로 변환합니다.
        row = binary_str.replace('1', '#').replace('0', ' ')
        answer.append(row)
        
    return answer

# --- 예시 테스트 ---
n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

print(solution(n, arr1, arr2))