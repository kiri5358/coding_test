from collections import Counter

def solution(lines):
    segments = []

    for start, end in lines:
        segments.extend(range(start, end))
    
    count = Counter(segments)
    
    answer = sum(1 for seg, c in count.items() if c >= 2)
    
    return answer