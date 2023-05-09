def remove_duplicates(nums: list[int]) -> int:
    """
    Given an integer array nums sorted in non-decreasing order,
    remove the duplicates in-place such that each unique element
    appears only once. The relative order of the elements should be
    kept the same. Then return the number of unique elements in nums.

    Consider the number of unique elements of nums to be k, to get
    accepted, you need to do the following things:

    1. Change the array nums such that the first k elements of nums
    contain the unique elements in the order they were present in nums
    initially. The remaining elements of nums are not important as well
    as the size of nums.

    2. Return k.
    :param nums: integer array sorted in non-decreasing order
    :return: the number of unique elements in nums.
    """
    k = set(nums)
    k = list(k)
    k.sort()

    for i in range(len(k)):
        nums[i] = k[i]
    return len(k)


nums1 = [1, 1, 2]
output_1 = 2
nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
output_2 = 5
"""
Constraints:

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
"""


def test(nums, output):
    if remove_duplicates(nums) == output:
        print("test - ok", nums)
    else:
        print("Test failed", nums)


test(nums1, output_1)
test(nums2, output_2)
