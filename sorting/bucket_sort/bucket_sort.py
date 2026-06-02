from insertion_sort import insertion_sort


def bucket_sort(nums: list) -> list:
    max_num = max(nums)
    min_num = min(nums)
    bucket_width = (max_num - min_num) // len(nums)

    buckets = [[] for _ in range(len(nums))]
    for num in nums:
        bucket_index = (num - min_num) // bucket_width
        if num == max_num:
            bucket_index -= 1

        buckets[bucket_index].append(num)

    sorted_list = []
    for bucket in buckets:
        if bucket:
            sorted_list += insertion_sort(bucket)

    return sorted_list


nums = [64, 34, 25, 12, 22, 11, 90]
print(f"{bucket_sort(nums)=}")
