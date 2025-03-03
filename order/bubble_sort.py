def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        flag = False
        for j in range(0, i):
            if arr[j+1] < arr[j]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
                flag = True
        if not flag:
            break
    return arr

def recusive_bubble_sort(arr, size_n):
    if size_n == 1:
        return
    for i in range(0, size_n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    recusive_bubble_sort(arr, size_n-1)


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    arr = [3, 7, 6, 4, 5, 1, 2, 8]
    print(bubble_sort(arr))
    
    arr = [12, 11, 13, 5, 6]
    arr = [3, 7, 6, 4, 5, 1, 2, 8]
    recusive_bubble_sort(arr, len(arr))
    print(arr)