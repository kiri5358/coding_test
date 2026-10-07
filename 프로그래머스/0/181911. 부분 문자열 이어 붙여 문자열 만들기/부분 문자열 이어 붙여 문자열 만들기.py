def solution(my_strings, parts):
  # 1. 결과를 담을 빈 문자열을 선언합니다.
  result = ''

  # 2. 인덱스를 직접 사용하기 위해 range와 len을 활용합니다.
  for i in range(len(my_strings)):
    text = my_strings[i]  # i번째 문자열
    s = parts[i][0]  # 시작 인덱스
    e = parts[i][1]  # 끝 인덱스

    # 3. 슬라이싱으로 부분 문자열을 추출한 뒤, result에 계속 더해줍니다.
    result += text[s : e + 1]

  return result