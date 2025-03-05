def bucket_sort(arr):
    min_val = min(arr)
    max_val = max(arr)
    bucket_size = 5
    bucket_count = (max_val - min_val) // bucket_size + 1
    buckets = [[] for _ in range(bucket_count)]
    for i in arr:
        idx = (i - min_val) // bucket_size
        buckets[idx].append(i)

    sorted_arr = []
    for i in buckets:
        sorted_arr.extend(sorted(i))

    return sorted_arr


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    print(bucket_sort(arr))

    arr = [3, 7, 6, 4, 5, 1, 2, 8]
    print(bucket_sort(arr))