def solution(babbling):
    answer = 0
    speakable = ["aya", "ye", "woo", "ma"]
    
    for b in babbling:
        # 1. 연속된 발음이 있는지 확인
        is_invalid = False
        for s in speakable:
            if s * 2 in b:  # 예: "ayaaya"가 문자열에 포함되어 있는지 확인
                is_invalid = True
                break
                
        if is_invalid:
            continue
            
        # 2. 가능한 발음들을 공백(" ")으로 치환
        for s in speakable:
            b = b.replace(s, " ")
            
        # 3. 공백을 모두 제거했을 때 빈 문자열만 남으면 발음 가능한 단어
        if b.strip() == "":
            answer += 1
            
    return answer