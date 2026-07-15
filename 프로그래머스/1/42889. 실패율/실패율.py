def solution(N, stages):
    total_players = len(stages)
    fail_rates = []
    
    for stage in range(1, N + 1):
        current_players = stages.count(stage)
        
        if total_players == 0:
            rate = 0
        else:
            rate = current_players / total_players
            
        fail_rates.append([stage, rate])
        
        total_players -= current_players
        
    fail_rates.sort(key=lambda x: (-x[1], x[0]))
    
    answer = [stage[0] for stage in fail_rates]
    return answer