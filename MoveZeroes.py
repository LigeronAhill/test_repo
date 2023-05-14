def main():
    test()


nums1 = [0, 1, 0, 3, 12]
nums2 = [0]


def test():
    if move_zeroes(nums1) == [1, 3, 12, 0, 0]:
        print("Test 1 - ok")
    else:
        print(f"Test 1 failed with {move_zeroes(nums1)}")
    if move_zeroes(nums2) == [0]:
        print("Test 2 - ok")
    else:
        print(f"Test 2 failed with {move_zeroes(nums2)}")


def move_zeroes(nums: list[int]):
    """
    Given an integer array nums, move all 0's to the end of it while maintaining
    the relative order of the non-zero elements.
    Note that you must do this in-place without making a copy of the array.
    Constraints:
    1 <= nums.length <= 104
    -2**31 <= nums[i] <= 2**31 - 1
    :param nums: list[int]
    :return:None
    """

    # return None
    return nums


if __name__ == "__main__":
    main()