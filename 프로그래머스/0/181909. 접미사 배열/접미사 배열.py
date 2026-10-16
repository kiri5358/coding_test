def solution(my_string):
    # 1. 인덱스 0부터 끝까지 순회하며 모든 접미사 추출
    suffixes = [my_string[i:] for i in range(len(my_string))]
    
    # 2. 사전순으로 정렬하여 반환
    return sorted(suffixes)