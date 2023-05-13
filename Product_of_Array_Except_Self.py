def product_except_self(nums: list[int]) -> list[int]:
    """
    Given an integer array nums, return an array answer
    such that answer[i] is equal to the product of all the
    elements of nums except nums[i].
    The product of any prefix or suffix of nums is guaranteed
    to fit in a 32-bit integer.
    You must write an algorithm that runs in O(n) time and without
    using the division operation.
    Constraints:
    1. 2 <= nums.length <= 105
    2. -30 <= nums[i] <= 30
    3.The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
    :param nums: list
    :return: list
    """

    prefix = [1]*len(nums)
    suffix = [1]*len(nums)
    result = [0]*len(nums)

    for i in range(1, len(nums)):
        prefix[i] = prefix[i-1]*nums[i-1]

    for i in range(len(nums)-2, -1, -1):
        suffix[i] = suffix[i+1]*nums[i+1]

    for i in range(len(nums)):
        result[i] = suffix[i]*prefix[i]

    return result


def second_variant(nums):
    result = [1]
    prefix = 1
    suffix = 1
    for i in range(1, len(nums)):
        prefix *= nums[i-1]
        result.append(prefix)
    for i in range(len(nums)-2, -1, -1):
        suffix *= nums[i+1]
        result[i] *= suffix
    return result


def test():
    if product_except_self(example_1) == output_1:
        print("Test 1 - ok")
    else:
        print(f"Test 1 failed. Output = {product_except_self(example_1)}")

    if product_except_self(example_2) == output_2:
        print("Test 2 - ok")
    else:
        print(f"Test 2 failed. Output = {product_except_self(example_2)}")

    if second_variant(example_1) == output_1:
        print("Test 3 - ok")
    else:
        print(f"Test 3 failed. Output = {second_variant(example_1)}")

    if second_variant(example_2) == output_2:
        print("Test 4 - ok")
    else:
        print(f"Test 4 failed. Output = {second_variant(example_2)}")


example_1 = [1, 2, 3, 4]
example_2 = [-1, 1, 0, -3, 3]
output_1 = [24, 12, 8, 6]
output_2 = [0, 0, 9, 0, 0]


if __name__ == "__main__":
    test()
