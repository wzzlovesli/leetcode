def counting_sort(arr):
    max_val = max(arr)
    count_arr = [0] * (max_val + 1)
    for i in arr:
        count_arr[i] += 1

    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]

    sorted_arr = [0] * len(arr)
    for i in arr:
        sorted_arr[count_arr[i] - 1] = i
        count_arr[i] -= 1

    return sorted_arr


def counting_sort_min_max(arr):
    min_val = min(arr)
    max_val = max(arr)
    count_arr = [0] * (max_val - min_val + 1)
    for i in arr:
        count_arr[i - min_val] += 1

    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]

    sorted_arr = [0] * len(arr)
    for i in arr:
        sorted_arr[count_arr[i - min_val] - 1] = i
        count_arr[i - min_val] -= 1

    return sorted_arr


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    print(counting_sort(arr))

    arr = [3, 7, 6, 4, 5, 1, 2, 8]
    print(counting_sort(arr))