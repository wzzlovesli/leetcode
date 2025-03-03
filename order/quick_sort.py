def quick_sort(arr, left, right):
    if left >= right:
        return
    # Choose random pivot to avoid worst case
    # pivot_idx = random.randint(left, right)
    # arr[pivot_idx], arr[right] = arr[right], arr[pivot_idx]

    pivot = partition(arr, left, right)
    quick_sort(arr, left, pivot - 1)
    quick_sort(arr, pivot + 1, right)


def partition(arr, left, right):
    pivot = right
    # Location of pivot after partition
    location = left

    for i in range(left, right):
        if arr[i] < arr[pivot]:
            arr[location], arr[i] = arr[i], arr[location]

            location += 1
    arr[pivot], arr[location] = arr[location], arr[pivot]

    return location


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)

    arr = [3, 7, 6, 4, 5, 1, 2, 8]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)
