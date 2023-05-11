def can_place_flowers(flowerbed: list[int], n: int):
    """
    You have a long flowerbed in which some of the plots are planted,
    and some are not. However, flowers cannot be planted in adjacent plots.
    Given an integer array flowerbed containing 0's and 1's, where 0 means
    empty and 1 means not empty, and an integer n, return true if n new flowers
    can be planted in the flowerbed without violating the
    no-adjacent-flowers rule and false otherwise.
    :param flowerbed: Integer array containing 0's and 1's
    :param n: new flowers to plant.
    :return: True if n new flowers can be planted and false otherwise.
    Constraints:
        1 <= flowerbed.length <= 2 * 104
        flowerbed[i] is 0 or 1.
        There are no two adjacent flowers in flowerbed.
        0 <= n <= flowerbed.length
    """
    if n == 0:
        return True
    elif n == 1 and len(flowerbed) == 1:
        if flowerbed[0] != 0:
            return False
        else:
            return True

    if flowerbed[0] == 0 and flowerbed[1] == 0:
        flowerbed[0] = 1
        n -= 1
        if n == 0:
            return True
    if flowerbed[-1] == 0 and flowerbed[-2] == 0:
        flowerbed[-1] = 1
        n -= 1
        if n == 0:
            return True
    for i in range(1, len(flowerbed)-1):
        if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
            flowerbed[i] = 1
            n -= 1
            if n == 0:
                return True
    return False


test1_input1 = [1, 0, 0, 0, 1]
test1_input2 = 1
test1_output = True

test2_input1 = [1, 0, 0, 0, 1]
test2_input2 = 2
test2_output = False

test3_input1 = [0, 0, 1, 0, 1]
test3_input2 = 1
test3_output = True

test4_input1 = [1, 0, 0, 0, 1, 0, 0]
test4_input2 = 2
test4_output = True


def test(test_input1, test_input2, test_output, n):
    if can_place_flowers(test_input1, test_input2) == test_output:
        print(f"Test {n} - ok")
    else:
        print(f"Test {n} failed. Result = {can_place_flowers(test_input1, test_input2)}")


if __name__ == "__main__":
    test(test1_input1, test1_input2, test1_output, 1)
    test(test2_input1, test2_input2, test2_output, 2)
    test(test3_input1, test3_input2, test3_output, 3)
    test(test4_input1, test4_input2, test4_output, 4)
