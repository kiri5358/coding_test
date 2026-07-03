def solution(cards1, cards2, goal):
    idx1 = 0
    idx2 = 0

    for word in goal:
        if idx1 < len(cards1) and cards1[idx1] == word:
            idx1 += 1 # cards1의 포인터를 다음으로 이동
            
        elif idx2 < len(cards2) and cards2[idx2] == word:
            idx2 += 1 # cards2의 포인터를 다음으로 이동
            
        else:
            return "No"
            
    return "Yes"