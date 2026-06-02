def solution(board):
    n = len(board)
    
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    
    mines = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                mines.append((i, j))
                
    for x, y in mines:
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == 0:
                    board[nx][ny] = 2
                    
    answer = 0
    for row in board:
        answer += row.count(0)
        
    return answer