def solution(arr, queries):
    answer = []
    
    for s, e, k in queries:
        # s부터 e까지의 범위에서 k보다 큰 값들을 필터링
        filtered = [arr[i] for i in range(s, e + 1) if arr[i] > k]
        
        # 조건을 만족하는 값이 있다면 최솟값, 없다면 -1 저장
        if filtered:
            answer.append(min(filtered))
        else:
            answer.append(-1)
            
    return answer