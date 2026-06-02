def binary_search(target: int, nums: list) -> int:
    if target < nums[0] or target > nums[-1]:
        return None

    left_pointer = 0
    right_pointer = len(nums) - 1

    while left_pointer <= right_pointer:
        mid = (left_pointer + right_pointer) // 2

        if target == nums[mid]:
            return mid

        if target < nums[mid]:
            right_pointer = mid - 1

        if target > nums[mid]:
            left_pointer = mid + 1

    return None


target = 90
nums = [11, 12, 22, 25, 34, 64, 90]

print(binary_search(11, nums))  # first element → expect 0
print(binary_search(90, nums))  # last element → expect 6
print(binary_search(25, nums))  # middle element → expect 3
print(binary_search(50, nums))  # not in list → expect None
print(binary_search(5, nums))  # below range → expect None
print(binary_search(100, nums))  # above range → expect None
