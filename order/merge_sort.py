def merge_sort(arr, left, right):
    if left >= right:
        return

    mid = left + (right - left) // 2
    merge_sort(arr, left, mid)
    merge_sort(arr, mid + 1, right)

    merge(arr, left, mid, right)


def merge(arr, left, mid, right):
    tmp = []
    i = left
    j = mid + 1

    # Merge the two sorted halves
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1

    # Add remaining elements from left half
    while i <= mid:
        tmp.append(arr[i])
        i += 1

    # Add remaining elements from right half
    while j <= right:
        tmp.append(arr[j])
        j += 1

    # Copy back to original array
    for i in range(len(tmp)):
        arr[left + i] = tmp[i]


def merge_sort_iterative(arr):
    n = len(arr)
    # curr_size is the size of subarray to be merged
    curr_size = 1

    while curr_size < n:
        left = 0
        while left < n - 1:
            mid = min(left + curr_size - 1, n - 1)
            right = min(left + 2 * curr_size - 1, n - 1)

            merge(arr, left, mid, right)
            left += 2 * curr_size

        curr_size *= 2


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    merge_sort(arr, 0, len(arr) - 1)
    print(arr)

    arr = [3, 7, 6, 4, 5, 1, 2, 8]
    merge_sort(arr, 0, len(arr) - 1)
    print(arr)
