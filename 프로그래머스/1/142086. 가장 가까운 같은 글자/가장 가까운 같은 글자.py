def solution(s):
    answer = []
    last_seen = {}  # 문자의 최근 등장 인덱스를 저장할 딕셔너리
    
    for i, char in enumerate(s):
        if char in last_seen:
            # 현재 인덱스 - 직전에 등장했던 인덱스
            answer.append(i - last_seen[char])
        else:
            # 처음 등장하는 문자
            answer.append(-1)
            
        # 현재 문자의 위치를 가장 최근 위치로 갱신
        last_seen[char] = i
        
    return answer