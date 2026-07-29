def solution(s, skip, index):
    # 1. 알파벳 소문자 리스트를 만듭니다 ('a'부터 'z'까지)
    # 2. skip에 포함된 알파벳들은 제외합니다
    alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    valid_chars = [c for c in alphabet if c not in skip]
    
    answer = ''
    
    # 3. 문자열 s의 각 문자를 순회합니다
    for char in s:
        # 현재 문자의 valid_chars에서의 위치(인덱스)를 찾습니다
        curr_idx = valid_chars.index(char)
        
        # index만큼 뒤로 이동하되, 리스트의 길이를 넘어가면 처음으로 돌아오도록 나머지 연산(%)을 사용합니다
        new_idx = (curr_idx + index) % len(valid_chars)
        
        # 변환된 문자를 결과에 추가합니다
        answer += valid_chars[new_idx]
        
    return answer