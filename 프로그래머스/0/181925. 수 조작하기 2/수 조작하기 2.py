def solution(numLog):
    mapping = {1: "w", -1: "s", 10: "d", -10: "a"}
    result = []
    
    for i in range(1, len(numLog)):
        diff = numLog[i] - numLog[i - 1]
        result.append(mapping[diff])
        
    return "".join(result)