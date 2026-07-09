def solution(n, m, section):
    answer = 0
    # 현재까지 페인트가 칠해진 가장 오른쪽 끝 위치
    painted_until = 0
    
    for s in section:
        # 현재 칠해야 할 구역이 기존에 칠한 범위를 벗어났다면
        if s > painted_until:
            # 새로운 페인트칠 시작! 횟수를 1 증가시킵니다.
            answer += 1
            # 롤러의 길이(m)만큼 칠해지므로, 칠해진 끝 위치를 갱신합니다.
            # (s번 구역부터 시작해서 m개의 구역을 칠하므로 s + m - 1 까지 칠해집니다)
            painted_until = s + m - 1
            
    return answer