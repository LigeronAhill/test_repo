def is_subsequence(s: str, t: str) -> bool:
    """
    Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
    A subsequence of a string is a new string that is formed from the original string by
    deleting some (can be none) of the characters without disturbing the relative positions
    of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
    :param s:subsequence
    :param t:string
    :return:bool
    """
    left, right = 0, 0
    while left < len(s) and right < len(t):
        if s[left] == t[right]:
            left += 1
        right += 1
    return left == len(s)


def test():
    if is_subsequence("abc", "ahbgdc"):
        print(f'Test 1 - ok. Answer - "{is_subsequence("abc", "ahbgdc")}"')
    else:
        print(f'Test 1 failed with "{is_subsequence("abc", "ahbgdc")}"')
    if not is_subsequence("axc", "ahbgdc"):
        print(f'Test 2 - ok. Answer - "{is_subsequence("axc", "ahbgdc")}"')
    else:
        print(f'Test 2 failed with "{is_subsequence("axc", "ahbgdc")}"')


def main():
    test()


if __name__ == "__main__":
    main()
