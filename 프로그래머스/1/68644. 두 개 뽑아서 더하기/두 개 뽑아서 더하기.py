def solution(numbers):
    answer_set = set()
    
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            answer_set.add(numbers[i] + numbers[j])
            
    return sorted(list(answer_set))