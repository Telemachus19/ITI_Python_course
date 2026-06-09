def rm_adj(lst):
    if not lst:
        return []
    
    result = [lst[0]]
    
    for i in range(1, len(lst)):
        if lst[i] != lst[i - 1]:
            result.append(lst[i])
    
    return result

arr = [1,2,3,3,4,4,5]
print(arr)
print(rm_adj(arr))