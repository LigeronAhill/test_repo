def find_max_average(nums: list[int], k: int) -> float:
    """
    You are given an integer array nums consisting of n elements, and an integer k.
    Find a contiguous subarray whose length is equal to k that has the maximum average
    value and return this value. Any answer with a calculation error less than 10**-5 will be accepted.
    Constraints:
    n == nums.length
    1 <= k <= n <= 10**5
    -10**4 <= nums[i] <= 10**4
    :param nums: integer array
    :param k: integer
    :return: maximum average value of a contiguous subarray whose length is equal to k
    """
    if len(nums) < 1 or len(nums) > 10**5:
        raise ValueError('incorrect value')
    if k < 1 or k > 10**5:
        raise ValueError('incorrect value')
    if min(nums) < -10**4 or max(nums) > 10**4:
        raise ValueError('incorrect list')

    max_sum = sum(nums[:k])
    curr_sum = max_sum

    for i in range(1, len(nums) - k + 1):
        curr_sum = curr_sum - nums[i - 1] + nums[i + k - 1]
        max_sum = max(max_sum, curr_sum)

    return max_sum / k


def test():
    print("Test 1 - ok" if find_max_average([1, 12, -5, -6, 50, 3], 4) == 12.75 else "Test 1 failed", find_max_average([1, 12, -5, -6, 50, 3], 4))
    print("Test 2 - ok" if find_max_average([0, 1, 1, 3, 3], 4) == 2 else "Test 2 failed", find_max_average([0, 1, 1, 3, 3], 4))


def main():
    test()


if __name__ == "__main__":
    main()
