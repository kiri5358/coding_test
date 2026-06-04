import math

def solution(numer1, denom1, numer2, denom2):

    result_numer = (numer1 * denom2) + (numer2 * denom1)
    result_denom = denom1 * denom2
    
    current_gcd = math.gcd(result_numer, result_denom)
    
    final_numer = result_numer // current_gcd
    final_denom = result_denom // current_gcd
    
    return [final_numer, final_denom]