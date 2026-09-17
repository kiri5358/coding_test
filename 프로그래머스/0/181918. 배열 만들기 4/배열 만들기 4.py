def solution(arr):
    stk = []
    i = 0
    while i < len(arr):
        # stk가 빈 배열인 경우
        if not stk:
            stk.append(arr[i])
            i += 1
        # stk의 마지막 원소가 arr[i]보다 작은 경우
        elif stk[-1] < arr[i]:
            stk.append(arr[i])
            i += 1
        # stk의 마지막 원소가 arr[i]보다 크거나 같은 경우
        else:
            stk.pop()
            
    return stk