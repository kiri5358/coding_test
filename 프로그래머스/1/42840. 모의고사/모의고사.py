def solution(answers):
    # 1. 수포자들의 찍기 패턴 정의
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    # 2. 맞힌 개수를 저장할 점수 리스트
    scores = [0, 0, 0]
    
    # 3. 정답 배열을 순회하며 각 수포자의 답과 비교
    for idx, answer in enumerate(answers):
        if answer == pattern1[idx % len(pattern1)]:
            scores[0] += 1
        if answer == pattern2[idx % len(pattern2)]:
            scores[1] += 1
        if answer == pattern3[idx % len(pattern3)]:
            scores[2] += 1
            
    # 4. 가장 높은 점수 계산
    max_score = max(scores)
    
    # 5. 가장 많이 맞힌 사람(들)을 찾아 결과 배열에 추가 (1번 인덱스부터 시작하므로 i+1)
    result = []
    for i, score in enumerate(scores):
        if score == max_score:
            result.append(i + 1)
            
    return result