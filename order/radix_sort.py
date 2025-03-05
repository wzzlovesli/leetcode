def radix_sort(arr):
    max_val = max(arr)
    
    # counting_sort(arr, exp) will sort the array based on the digit at the exp place
    def counting_sort(arr, exp):
        n = len(arr)
        output = [0] * n
        count = [0] * 10
        for i in range(0, n):
            idx = arr[i] // exp
            count[idx % 10] += 1
        for i in range(1, 10):
            count[i] += count[i - 1]
        i = n - 1
        while i >= 0:
            idx = arr[i] // exp
            output[count[idx % 10] - 1] = arr[i]
            count[idx % 10] -= 1
            i -= 1
        for i in range(0, n):
            arr[i] = output[i]
    
    exp = 1
    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr

if __name__ == "__main__":
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    print(radix_sort(arr))

    arr = [170, 45, 75, 90, 802, 24, 2, 66, 1000]
    print(radix_sort(arr))