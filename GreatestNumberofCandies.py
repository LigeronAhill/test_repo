def kids_with_candies(candies: list[int], extracandies: int):
    """
    There are n kids with candies. You are given an integer array candies,
    where each candies[i] represents the number of candies the ith kid has,
    and an integer extraCandies, denoting the number of extra candies that you have.
    Return a boolean array result of length n, where result[i] is true if,
    after giving the ith kid all the extraCandies, they will have the greatest
    number of candies among all the kids, or false otherwise.
    Note that multiple kids can have the greatest number of candies.
    :param candies: A list of candy that kids have.
    :param extracandies: The number of extra candies that you have.
    :return: A boolean array result of length n.
    """
    result = []
    for i in range(len(candies)):
        if candies[i] + extracandies >= max(candies):
            result.append(True)
        else:
            result.append(False)

    return result


def main():
    test()


def test():
    test_1_candies = [2, 3, 5, 1, 3]
    test_1_extra_candies = 3
    output_1 = [True, True, True, False, True]

    test_2_candies = [4, 2, 1, 1, 2]
    test_2_extra_candies = 1
    output_2 = [True, False, False, False, False]

    test_3_candies = [12, 1, 12]
    test_3_extra_candies = 10
    output_3 = [True, False, True]

    if kids_with_candies(test_1_candies, test_1_extra_candies) == output_1:
        print("test 1 - ok")
    else:
        print(f"test 1 failed with {kids_with_candies(test_1_candies, test_1_extra_candies)}")

    if kids_with_candies(test_2_candies, test_2_extra_candies) == output_2:
        print("test 2 - ok")
    else:
        print(f"test 2 failed with {kids_with_candies(test_2_candies, test_2_extra_candies)}")

    if kids_with_candies(test_3_candies, test_3_extra_candies) == output_3:
        print("test 3 - ok")
    else:
        print(f"test 3 failed with {kids_with_candies(test_3_candies, test_3_extra_candies)}")


if __name__ == "__main__":
    main()
