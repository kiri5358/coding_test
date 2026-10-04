def solution(my_string, queries):
    # 문자열은 불변(immutable)이므로 리스트로 변환하여 처리합니다.
    my_list = list(my_string)
    
    for s, e in queries:
        # 인덱스 s부터 e까지의 부분을 뒤집어서 다시 제자리에 넣습니다.
        my_list[s:e+1] = my_list[s:e+1][::-1]
        
    return ''.join(my_list)