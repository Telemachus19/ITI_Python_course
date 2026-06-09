def bubble(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

arr = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted array:", arr)
sorted_arr = bubble(arr)
print("Sorted array:", sorted_arr)

# there is also sorted() :-)

print("sorted array using sorted():", sorted(arr))