def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        # start from gap
        for i in range(gap, n): 
            curr = arr[i]
            j = i
            while j >= gap and arr[j - gap] > curr:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = curr
        gap //= 2
    return arr


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    print(shell_sort(arr))

    arr = [3, 7, 6, 4, 5, 1, 2, 8]
    print(shell_sort(arr))