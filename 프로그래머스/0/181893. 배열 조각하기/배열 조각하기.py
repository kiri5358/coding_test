def solution(arr, query):
    for i in range(len(query)):
        v = query[i]
        if i % 2 == 0:
            # 짝수 인덱스: query[i]번 인덱스의 뒷부분을 자름 (앞부분만 남김)
            arr = arr[:v + 1]
        else:
            # 홀수 인덱스: query[i]번 인덱스의 앞부분을 자름 (뒷부분만 남김)
            arr = arr[v:]
            
    return arr