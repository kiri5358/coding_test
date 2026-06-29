def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        sliced = array[i-1:j]
        sorted_array = sorted(sliced)
        answer.append(sorted_array[k-1])
    return answer