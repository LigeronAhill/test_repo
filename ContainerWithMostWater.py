def max_area(height: list[int]) -> int:
    """
    You are given an integer array height of length n.
    There are n vertical lines drawn such that the two endpoints
    of the ith line are (i, 0) and (i, height[i]).
    Find two lines that together with the x-axis form a container,
    such that the container contains the most water.
    Return the maximum amount of water a container can store.
    Notice that you may not slant the container.
    :param height: list of heights
    :return: square[int]
    """
    if len(height) <= 1:
        return 0
    left = 0
    right = len(height) - 1
    square = 0
    while left < right:
        tmp_area = min(height[left], height[right])*(right-left)
        square = max(square, tmp_area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return square


def test():
    if max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49:
        print("Test 1 - ok")
    else:
        print(f"Test 1 failed with {max_area([1, 8, 6, 2, 5, 4, 8, 3, 7])}")
    if max_area([1, 1]) == 1:
        print("Test 2 - ok")
    else:
        print(f"Test 2 failed with {max_area([1, 1])}")


def main():
    test()


if __name__ == "__main__":
    main()
