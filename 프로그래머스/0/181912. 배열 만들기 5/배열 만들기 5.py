def solution(intStrs, k, s, l):
    answer = []
    for int_str in intStrs:
        # s번 인덱스에서 시작하여 길이 l만큼 부분 문자열을 잘라낸 뒤 정수로 변환
        val = int(int_str[s:s+l])
        # 변환한 값이 k보다 크면 결과 배열에 추가
        if val > k:
            answer.append(val)
    return answer