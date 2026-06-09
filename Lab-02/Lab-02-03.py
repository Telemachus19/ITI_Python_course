def different(lst):
    # using a set is easier here, but the naive solution is to use two nested loops to compare each element with every other element
    seen = set()
    for num in lst:
        if num in seen:
            return False
        seen.add(num)
    return True