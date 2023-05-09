def remove_duplicates(input_nums: list[int]) -> int:
    """
    Given an integer array nums sorted in non-decreasing order,
    remove the duplicates in-place such that each unique element
    appears only once. The relative order of the elements should be
    kept the same. Then return the number of unique elements in nums.

    Consider the number of unique elements of nums to be k, to get
    accepted, you need to do the following things:

    - Change the array nums such that the first k elements of nums
    contain the unique elements in the order they were present in nums
    initially. The remaining elements of nums are not important as well
    as the size of nums.

    - Return k.
    :param input_nums: integer array sorted in non-decreasing order
    :return: the number of unique elements in nums.
    """
    return 0


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
        print("test - ok")
    else:
        print("Test failed")


test(nums1, output_1)
test(nums2, output_2)
