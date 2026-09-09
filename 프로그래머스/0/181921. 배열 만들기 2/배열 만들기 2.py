def solution(l, r):
    answer = []
    for num in range(l, r + 1):
        if all(char in '05' for char in str(num)):
            answer.append(num)
    return answer if answer else [-1]