import math

def solution(num_list):
    total_product = math.prod(num_list)
    total_sum_square = sum(num_list) ** 2
    
    if total_product < total_sum_square:
        return 1
    else:
        return 0