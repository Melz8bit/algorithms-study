def _merge(left_list: list, right_list: list) -> list:
    sorted_nums = []
    while left_list and right_list:
        if right_list[0] < left_list[0]:
            sorted_nums.append(right_list.pop(0))

        elif left_list[0] < right_list[0]:
            sorted_nums.append(left_list.pop(0))

        else:
            sorted_nums.append(left_list.pop(0))
            sorted_nums.append(right_list.pop(0))

    # Append any remaining items to the sorted list
    sorted_nums.extend(left_list)
    sorted_nums.extend(right_list)

    return sorted_nums


def merge_sort(nums: list, left_list: list = None, right_list: list = None) -> list:
    if not nums:
        return []

    if len(nums) == 1:
        return nums

    sorted_nums = []

    # Split list
    halfway = len(nums) // 2
    left_list = nums[0:halfway]
    right_list = nums[halfway:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)

    sorted_nums = _merge(left_list, right_list)

    return sorted_nums


nums = [2, 64, 34, 25, 12, 22, 11, 90]
print(f"Unsorted: {nums} \tSorted: {merge_sort(nums)}")
