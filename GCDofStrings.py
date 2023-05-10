def gcd_of_strings(str1: str, str2: str) -> str:
    """
    For two strings s and t, we say "t divides s" if and
    only if s = t + ... + t (i.e., t is concatenated with
    itself one or more times).
    Given two strings str1 and str2, return the largest
    string x such that x divides both str1 and str2.
    :param str1: 1 <= len(str1) <= 1000
    :param str2: 1 <= len(str2) <= 1000
    :return: greatest common divisor of both str1 and str2
    """
    for i in range(min(len(str1), len(str2)), 0, -1):
        if str2[:i] * (len(str1) // i) == str1 and str2[:i] * (len(str2) // i) == str2:
            return str2[:i]
    return ""


def test():
    test_1_str1 = "ABCABC"
    test_1_str2 = "ABC"
    output_1 = "ABC"

    test_2_str1 = "ABABAB"
    test_2_str2 = "ABAB"
    output_2 = "AB"

    test_3_str1 = "LEET"
    test_3_str2 = "CODE"
    output_3 = ""

    if gcd_of_strings(test_1_str1, test_1_str2) == output_1:
        print("test 1 - ok")
    else:
        print(f"test 1 failed with {gcd_of_strings(test_1_str1, test_1_str2)}")

    if gcd_of_strings(test_2_str1, test_2_str2) == output_2:
        print("test 2 - ok")
    else:
        print(f"test 2 failed with {gcd_of_strings(test_2_str1, test_2_str2)}")

    if gcd_of_strings(test_3_str1, test_3_str2) == output_3:
        print("test 3 - ok")
    else:
        print(f"test 3 failed with {gcd_of_strings(test_3_str1, test_3_str2)}")


def main():
    test()


if __name__ == "__main__":
    main()
