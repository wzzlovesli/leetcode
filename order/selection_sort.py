def selection_sort(arr):
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp
    return arr


def selection_sort2(arr):
    for i in range(0, len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # tmp = arr[i]
        # arr[i] = arr[min_idx]
        # arr[min_idx] = tmp
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    print(selection_sort(arr))
    print(selection_sort2(arr))
