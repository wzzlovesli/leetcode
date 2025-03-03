def insert_sort(arr):
    for i in range(1, len(arr)):
        curr = arr[i]
        j = i - 1
        while j >= 0 and curr < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = curr
    return arr


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    print(insert_sort(arr))
