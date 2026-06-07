def solution(n):
    answer = [[0] * n for _ in range(n)]
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    x, y, dir_idx = 0, 0, 0
    
    for num in range(1, n**2 + 1):
        answer[x][y] = num
        
        nx = x + dx[dir_idx]
        ny = y + dy[dir_idx]
        
        if nx < 0 or nx >= n or ny < 0 or ny >= n or answer[nx][ny] != 0:
            dir_idx = (dir_idx + 1) % 4  # 0 -> 1 -> 2 -> 3 -> 0 순환
            nx = x + dx[dir_idx]
            ny = y + dy[dir_idx]
        
        x, y = nx, ny
        
    return answer