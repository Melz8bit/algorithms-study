def bubble_sort(nums):
    for _ in nums:
        had_swap = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                had_swap = True

        if not had_swap:
            break

    return nums


nums = [64, 34, 25, 12, 22, 11, 90]
nums2 = [11, 12, 22, 25, 34, 64, 90]

print(f"{nums=}: {bubble_sort(nums)}")
print(f"{nums2=}: {bubble_sort(nums2)}")
