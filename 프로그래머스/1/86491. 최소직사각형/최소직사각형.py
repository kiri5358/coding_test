def solution(sizes):
    max_w = 0  # 가장 큰 가로 길이를 저장할 변수
    max_h = 0  # 가장 큰 세로 길이를 저장할 변수
    
    for size in sizes:
        # 각 명함에서 [더 긴 길이, 더 짧은 길이]로 분리합니다.
        w = max(size)
        h = min(size)
        
        # 전체 명함 중 가장 큰 가로값과 세로값을 갱신합니다.
        if w > max_w:
            max_w = w
        if h > max_h:
            max_h = h
            
    return max_w * max_h