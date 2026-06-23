def solution(s, n):
    answer = []
    
    for char in s:
        # 공백은 밀지 않고 그대로 유지
        if char == " ":
            answer.append(" ")
        # 대문자인 경우
        elif char.isupper():
            # A의 아스키 코드(65)를 기준으로 n만큼 이동 후, 26(알파벳 개수)으로 나눈 나머지를 구함
            new_char = chr((ord(char) - ord('A') + n) % 26 + ord('A'))
            answer.append(new_char)
        # 소문자인 경우
        elif char.islower():
            # a의 아스키 코드(97)를 기준으로 n만큼 이동 후, 26으로 나눈 나머지를 구함
            new_char = chr((ord(char) - ord('a') + n) % 26 + ord('a'))
            answer.append(new_char)
            
    return "".join(answer)