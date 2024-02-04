def partition(arr, end, pivot):
    i = 0
    for j in range(end):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
    return i

arr = [14, 2, 6, 12, 10, 57, 13, 10, 6, 23, 3]
pivot = 10
subarray_size = partition(arr, len(arr), pivot)
print(arr)
partition(arr, subarray_size, pivot - 1)
print(arr)