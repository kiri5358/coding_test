def solution(nums):
    # 1. 내가 가져갈 수 있는 최대 마리 수 (N / 2)
    max_pick = len(nums) // 2
    
    # 2. set을 이용해 폰켓몬의 중복을 제거한 총 종류 수 구하기
    unique_types = len(set(nums))
    
    # 3. 두 값 중 더 작은 값을 반환
    return min(max_pick, unique_types)