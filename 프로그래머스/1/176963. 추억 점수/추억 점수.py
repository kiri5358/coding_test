def solution(name, yearning, photo):
    answer = []
    
    # 1. 이름과 그리움 점수를 매핑한 딕셔너리 생성
    score_map = {n: y for n, y in zip(name, yearning)}
    
    # 2. 각 사진을 순회하며 추억 점수 계산
    for p in photo:
        total_score = 0
        for person in p:
            # 딕셔너리에 이름이 있으면 점수를 더하고, 없으면 0을 더함
            total_score += score_map.get(person, 0)
        answer.append(total_score)
        
    return answer