def solution(a, b, c, d):
    dice = [a, b, c, d]
    counts = {}
    for num in dice:
        counts[num] = counts.get(num, 0) + 1
        
    sorted_keys = sorted(counts.keys(), key=lambda x: counts[x], reverse=True)
    
    if len(counts) == 1:
        p = sorted_keys[0]
        return 1111 * p
    
    elif len(counts) == 2:
        p = sorted_keys[0]
        q = sorted_keys[1]
        
        if counts[p] == 3:
            return (10 * p + q) ** 2
        else:
            return (p + q) * abs(p - q)
            
    elif len(counts) == 3:
        q = sorted_keys[1]
        r = sorted_keys[2]
        return q * r
        
    else:
        return min(dice)