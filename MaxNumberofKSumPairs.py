def main():
    test()


def test():
    if max_operations([1, 2, 3, 4], 5) == 2:
        print('Test 1 - ok')
    else:
        print(f'Test 1 failed with {max_operations([1, 2, 3, 4], 5)}')
    if max_operations([3, 1, 3, 4, 3], 6) == 1:
        print('Test 2 - ok')
    else:
        print(f'Test 2 failed with {max_operations([3, 1, 3, 4, 3], 6)}')


def max_operations(nums: list, k: int) -> int:
    """
    You are given an integer array nums and an integer k.
    In one operation, you can pick two numbers from the array
    whose sum equals k and remove them from the array.
    Return the maximum number of operations you can perform on the array.
    Constraints:
    1 <= nums.length <= 105
    1 <= nums[i] <= 109
    1 <= k <= 109
    :param nums: integer array
    :param k: sum to compare
    :return: maximum number of operations
    """
    # freq = {}
    # result = 0
    # for num in nums:
    #     if k-num in freq and freq[k-num] > 0:
    #         freq[k-num] -= 1
    #         result += 1
    #     else:
    #         freq[num] = freq.get(num, 0) + 1
    # return result

    result = 0
    left = 0
    right = len(nums) - 1
    nums.sort()

    while left < right:
        if nums[left] + nums[right] == k:
            result += 1
            left += 1
            right -= 1
        elif nums[left] + nums[right] < k:
            left += 1
        else:
            right -= 1
    return result


if __name__ == "__main__":
    main()
