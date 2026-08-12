def solution(babbling):
    answer = 0
    possible_words = ["aya", "ye", "woo", "ma"]
    
    for word in babbling:

        if "ayaaya" in word or "yeye" in word or "woowoo" in word or "mama" in word:
            continue

        for p in possible_words:
            word = word.replace(p, " ")

        if word.strip() == "":
            answer += 1
            
    return answer