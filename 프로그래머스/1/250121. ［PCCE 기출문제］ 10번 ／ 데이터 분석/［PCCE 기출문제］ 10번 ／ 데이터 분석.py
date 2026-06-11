def solution(data, ext, val_ext, sort_by):
    col_names = ["code", "date", "maximum", "remain"]
    ext_idx = col_names.index(ext)
    sort_idx = col_names.index(sort_by)
    
    filtered_data = [row for row in data if row[ext_idx] < val_ext]
    
    answer = sorted(filtered_data, key=lambda x: x[sort_idx])
    
    return answer