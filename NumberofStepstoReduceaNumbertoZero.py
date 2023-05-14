def main():
    test()


def test():
    if number_of_steps(14) == 6:
        print('Test 1  - ok')
    else:
        print(f'Test 1 failed with {number_of_steps(14)}')
    if number_of_steps(8) == 4:
        print('Test 2 - ok')
    else:
        print(f'Test 2 failed with {number_of_steps(8)}')


def number_of_steps(num: int) -> int:
    """
    Given an integer num, return the number of steps to reduce it to zero.
    In one step, if the current number is even, you have to divide it by 2,
    otherwise, you have to subtract 1 from it.
    :param num: integer
    :return: number of steps
    """
    result = 0
    while num != 0:
        if num % 2 == 0:
            num /= 2
            result += 1
        else:
            num -= 1
            result += 1
    return result


if __name__ == "__main__":
    main()
