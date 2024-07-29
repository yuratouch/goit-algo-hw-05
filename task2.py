def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = left + (right - left) // 2

        if arr[mid] == target:
            upper_bound = arr[mid]
            return (iterations, upper_bound)

        if arr[mid] < target:
            left = mid + 1
        else:
            upper_bound = arr[mid]
            right = mid - 1

    if upper_bound is None and left < len(arr):
        upper_bound = arr[left]

    return (iterations, upper_bound)

# Приклад використання
sorted_array = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7]
target = 4.0
result = binary_search(sorted_array, target)
print(result)  # Очікуваний вихід: (3, 4.4)
